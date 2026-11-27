import os
import re
from uuid import uuid4

import pytest
from werkzeug.security import generate_password_hash

from extracredit import create_app
from extracredit.db import connect, write
from extracredit.setup_db import SQL, build_schema, run_scripts

DEMO_PASSWORD = "just-a-test-password"


@pytest.fixture
def app(tmp_path):
    if os.getenv("RUN_DB_TESTS") != "1":
        pytest.skip("Set RUN_DB_TESTS=1 and configure the test MySQL connection.")
    name = f"extra_credit_test_{uuid4().hex}"
    app = create_app({
        "TESTING": True,
        "DEMO_MODE": True,
        "VERIFICATION_OUTBOX": tmp_path / "verification",
        "DB_NAME": name,
        "DB_HOST": os.getenv("TEST_DB_HOST", "127.0.0.1"),
        "DB_PORT": int(os.getenv("TEST_DB_PORT", "3306")),
        "DB_USER": os.getenv("TEST_DB_USER", "root"),
        "DB_PASSWORD": os.getenv("TEST_DB_PASSWORD", ""),
        "DB_SOCKET": os.getenv("TEST_DB_SOCKET", ""),
        "UPLOAD_DIR": tmp_path / "uploads",
    })
    created = False
    try:
        with app.app_context(), connect(database=False) as db:
            with db.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE `{name}` CHARACTER SET utf8mb4")
            created = True
            db.database = name
            build_schema(db)
            run_scripts(db, sorted((SQL / "seed").glob("*.sql")))
            password = generate_password_hash(DEMO_PASSWORD, method="pbkdf2:sha256:1000")
            write("UPDATE Students SET password_hash = %s", (password,), db)
        yield app
    finally:
        if created:
            with app.app_context(), connect(database=False) as db, db.cursor() as cursor:
                cursor.execute(f"DROP DATABASE `{name}`")


def csrf_token(client):
    html = client.get("/login").get_data(as_text=True)
    return re.search(r'<meta name="csrf-token" content="([^"]+)"', html).group(1)


@pytest.fixture
def sign_in(app):
    def make_client(name):
        client = app.test_client()
        response = client.post("/login", data={
            "email": f"{name}@example.com", "password": DEMO_PASSWORD, "csrf_token": csrf_token(client),
        })
        assert response.status_code == 302
        return client
    return make_client


@pytest.fixture
def api_write():
    def send(client, method, path, data=None, **kwargs):
        headers = {"X-CSRFToken": csrf_token(client)}
        if "content_type" in kwargs:
            return client.open(path, method=method, data=data, headers=headers, **kwargs)
        return client.open(path, method=method, json=data, headers=headers, **kwargs)
    return send
