from contextlib import contextmanager

import mysql.connector
from flask import current_app, g

from .common import AppError


def connect(database=True):
    config = current_app.config
    options = {
        "host": config["DB_HOST"],
        "port": config["DB_PORT"],
        "user": config["DB_USER"],
        "password": config["DB_PASSWORD"],
        "charset": "utf8mb4",
        "time_zone": "+00:00",
        "autocommit": True,
        "connection_timeout": 4,
    }
    if database:
        options["database"] = config["DB_NAME"]
    if config["DB_SOCKET"]:
        options["unix_socket"] = config["DB_SOCKET"]
    return mysql.connector.connect(**options)


def get_db():
    if "db" not in g:
        try:
            g.db = connect()
        except mysql.connector.Error as error:
            current_app.logger.warning("MySQL connection failed (code %s)", error.errno)
            raise AppError(503, "database_unavailable", "The database is unavailable. Try again shortly.") from error
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@contextmanager
def transaction():
    db = get_db()
    db.start_transaction()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise


def rows(sql, values=(), db=None):
    db = get_db() if db is None else db
    with db.cursor(dictionary=True) as cursor:
        cursor.execute(sql, values)
        return cursor.fetchall()


def first(sql, values=(), db=None):
    result = rows(sql, values, db)
    return result[0] if result else None


def write(sql, values=(), db=None):
    db = get_db() if db is None else db
    with db.cursor() as cursor:
        cursor.execute(sql, values)
        return cursor.lastrowid
