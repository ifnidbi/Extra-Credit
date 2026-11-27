from functools import wraps
import re

from flask import Blueprint, g, redirect, render_template, request, session, url_for
from mysql.connector import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from .common import AppError, api, form_data, invalid, text
from .db import first, write

bp = Blueprint("accounts", __name__)
PROFILE = "student_id, full_name, email, school_name, role"


def current_user():
    if "viewer" not in g:
        student_id = session.get("student_id")
        g.viewer = first(
            f"SELECT {PROFILE} FROM Students WHERE student_id = %s AND is_active",
            (student_id,),
        ) if student_id else None
    return g.viewer


def require_login(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not current_user():
            if request.path.startswith("/api/"):
                raise AppError(401, "sign_in", "Sign in to continue.")
            return redirect(url_for("accounts.login"))
        return view(*args, **kwargs)
    return wrapped


def require_admin(view):
    @wraps(view)
    @require_login
    def wrapped(*args, **kwargs):
        if current_user()["role"] != "admin":
            raise AppError(403, "forbidden", "An administrator is required.")
        return view(*args, **kwargs)
    return wrapped


def profile_fields(data):
    return text(data, "full_name", 100), text(data, "school_name", 150)


def register_account(data):
    full_name, school = profile_fields(data)
    email = text(data, "email", 150).lower()
    if not re.fullmatch(r"[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+", email):
        invalid("email", "Enter a valid email address.")
    password = data.get("password", "")
    if not isinstance(password, str) or not 12 <= len(password) <= 128:
        invalid("password", "Enter a password between 12 and 128 characters.")
    if data.get("student_attested") != "yes":
        invalid("student_attested", "Confirm that you are a student.")
    try:
        write(
            "INSERT INTO Students (full_name, email, password_hash, school_name) VALUES (%s, %s, %s, %s)",
            (full_name, email, generate_password_hash(password), school),
        )
    except IntegrityError as error:
        if error.errno != 1062:
            raise
        raise AppError(409, "duplicate_email", "An account already uses that email.") from error


@bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        try:
            register_account(request.form)
        except AppError as problem:
            error = problem
        else:
            return redirect(url_for("accounts.login", registered=1))
    return render_template("auth.html", register=True, error=error), error.status if error else 200


@bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = first("SELECT student_id, password_hash FROM Students WHERE email = %s AND is_active", (email,))
        if user and len(password) <= 128 and check_password_hash(user["password_hash"], password):
            session.clear()
            session["student_id"] = user["student_id"]
            return redirect(url_for("catalog.dashboard"))
        error = AppError(401, "invalid_login", "Check your email and password and try again.")
    return render_template("auth.html", register=False, error=error), error.status if error else 200


@bp.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("catalog.index"))


@bp.get("/account")
@require_login
def account_page():
    return render_template("account.html")


@bp.route("/api/account", methods=["GET", "PUT", "DELETE"])
@require_login
def account_api():
    user = current_user()
    student_id = user["student_id"]
    if request.method == "GET":
        return api(user)
    data = form_data()
    if request.method == "PUT":
        name, school = profile_fields(data)
        write("UPDATE Students SET full_name = %s, school_name = %s WHERE student_id = %s", (name, school, student_id))
        return api(first(f"SELECT {PROFILE} FROM Students WHERE student_id = %s", (student_id,)))
    if user["role"] == "admin":
        raise AppError(403, "forbidden", "Demo administrators are managed locally.")
    password = data.get("password", "")
    saved = first("SELECT password_hash FROM Students WHERE student_id = %s", (student_id,))
    if not isinstance(password, str) or len(password) > 128 or not check_password_hash(saved["password_hash"], password):
        invalid("password", "Enter your current password.")
    write("UPDATE Students SET is_active = FALSE WHERE student_id = %s", (student_id,))
    session.clear()
    return "", 204
