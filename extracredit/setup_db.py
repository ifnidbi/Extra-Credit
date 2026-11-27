from pathlib import Path
import re

import click
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from .db import connect, first, transaction, write

SQL = Path(__file__).resolve().parent.parent / "sql"


def run_scripts(db, paths):
    with db.cursor() as cursor:
        for path in paths:
            cursor.execute(path.read_text(encoding="utf-8"))
            while cursor.nextset():
                pass


def build_schema(db):
    run_scripts(db, sorted(SQL.glob("0[1-6]_*.sql")))
    run_scripts(db, sorted((SQL / "views").glob("*.sql")))


def seed():
    if current_app.config["DB_NAME"] not in {"extra_credit", "extra_credit_test"}:
        raise click.ClickException("Demo data is only allowed in extra_credit or extra_credit_test.")
    password = click.prompt("Password for fictional demo users", hide_input=True, confirmation_prompt=True)
    if len(password) < 12:
        raise click.ClickException("Use at least 12 characters.")
    with transaction() as db:
        if first("SELECT student_id FROM Students LIMIT 1", db=db):
            raise click.ClickException("Use an empty ExtraCredit database for the demo seed.")
        run_scripts(db, sorted((SQL / "seed").glob("*.sql")))
        for number in range(1, 7):
            write(
                "UPDATE Students SET password_hash = %s WHERE student_id = %s",
                (generate_password_hash(password), number),
                db,
            )
    click.echo("Demo data is ready. Try alex@example.com, priya@example.com, or admin@example.com.")


@click.command("init-db")
@with_appcontext
def init_db():
    name = current_app.config["DB_NAME"]
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,63}", name):
        raise click.ClickException("DB_NAME must start with a letter and contain only letters, numbers, or underscores.")
    with connect(database=False) as db:
        with db.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{name}` CHARACTER SET utf8mb4")
        db.database = name
        build_schema(db)
    click.echo(f"Schema and reports are ready in {name}.")


@click.command("seed-demo")
@with_appcontext
def seed_demo():
    seed()
