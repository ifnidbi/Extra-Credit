import os
from datetime import date
from pathlib import Path
from secrets import token_hex

from flask import Flask
from flask.json.provider import DefaultJSONProvider
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
from werkzeug.exceptions import HTTPException

from .common import AppError, error_response

csrf = CSRFProtect()


class AppJSON(DefaultJSONProvider):
    @staticmethod
    def default(value):
        if isinstance(value, date):
            return value.isoformat()
        return DefaultJSONProvider.default(value)


def create_app(test_config=None):
    app = Flask(__name__)
    app.json = AppJSON(app)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY") or token_hex(32),
        DB_HOST=os.getenv("DB_HOST", "127.0.0.1"),
        DB_PORT=int(os.getenv("DB_PORT", "3306")),
        DB_NAME=os.getenv("DB_NAME", "extra_credit"),
        DB_USER=os.getenv("DB_USER", "extra_credit_app"),
        DB_PASSWORD=os.getenv("DB_PASSWORD", ""),
        DB_SOCKET=os.getenv("DB_SOCKET", ""),
        UPLOAD_DIR=os.getenv("UPLOAD_DIR") or Path(app.instance_path) / "uploads",
        MAX_CONTENT_LENGTH=4 * 1024 * 1024,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=os.getenv("COOKIE_SECURE", "").lower() == "true",
    )
    if test_config is not None:
        app.config.update(test_config)

    from . import accounts, catalog, db, inquiries, photos, reports, weather
    from .routes import site
    from .setup_db import init_db, seed_demo

    csrf.init_app(app)
    app.teardown_appcontext(db.close_db)
    app.context_processor(lambda: {"viewer": accounts.current_user})
    app.cli.add_command(init_db)
    app.cli.add_command(seed_demo)
    for module in (site, accounts, catalog, inquiries, photos, reports, weather):
        app.register_blueprint(module.bp)

    @app.errorhandler(AppError)
    def app_error(error):
        return error_response(error.status, error.code, error.message, error.fields)

    @app.errorhandler(CSRFError)
    def csrf_error(error):
        return error_response(400, "csrf", "The form expired. Reload the page and try again.")

    @app.errorhandler(HTTPException)
    def http_error(error):
        if error.code == 500:
            return error_response(500, "server_error", "Something went wrong. Try again.")
        return error_response(error.code, error.name.lower().replace(" ", "_"), error.description)

    return app
