from functools import wraps
import re

from flask import Blueprint, current_app, g, redirect, render_template, request, session, url_for
from mysql.connector import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from .campus import DEMO_EMAILS, SCHOOL, STUDENT_DOMAIN
from .common import AppError, api, form_data, invalid, text
from .db import first, transaction, write
from .verification import read_verification_token, send_verification

bp = Blueprint("accounts", __name__)
PROFILE = "student_id, full_name, email, school_name, role"


def is_student_email(email):
    return re.fullmatch(r"[^\s@<>]+@" + re.escape(STUDENT_DOMAIN), email) is not None


def is_campus_account(user):
    return user and user["school_name"] == SCHOOL and (
        is_student_email(user["email"]) or (current_app.config["DEMO_MODE"] and user["email"] in DEMO_EMAILS)
    )


def current_user():
    if "viewer" not in g:
        student_id = session.get("student_id")
        user = first(
            f"SELECT {PROFILE} FROM Students WHERE student_id = %s AND is_active AND email_verified",
            (student_id,),
        ) if student_id else None
        g.viewer = user if is_campus_account(user) else None
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


def register_account(data):
    full_name = text(data, "full_name", 100)
    email = text(data, "email", 150).lower()
    if not is_student_email(email):
        invalid("email", "Use your Ontario Tech student email ending in @ontariotechu.net.")
    password = data.get("password", "")
    if not isinstance(password, str) or not 12 <= len(password) <= 128:
        invalid("password", "Enter a password between 12 and 128 characters.")
    if data.get("student_attested") != "yes":
        invalid("student_attested", "Confirm that you are a current Ontario Tech student.")
    try:
        password_hash = generate_password_hash(password)
        with transaction() as db:
            student_id = write(
                "INSERT INTO Students (full_name, email, password_hash, school_name) VALUES (%s, %s, %s, %s)",
                (full_name, email, password_hash, SCHOOL), db,
            )
            send_verification(student_id, email)
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
        error = AppError(401, "invalid_login", "Check your email and password and try again.")
        user = first(
            "SELECT student_id, email, school_name, password_hash, email_verified FROM Students WHERE email = %s AND is_active",
            (email,),
        )
        if is_campus_account(user) and len(password) <= 128 and check_password_hash(user["password_hash"], password):
            if user["email_verified"]:
                session.clear()
                session["student_id"] = user["student_id"]
                return redirect(url_for("catalog.index"))
            error = AppError(403, "unverified", "Confirm your Ontario Tech email before signing in.")
            if request.form.get("send_again") == "yes":
                send_verification(user["student_id"], user["email"])
                return redirect(url_for("accounts.login", registered=1))
    return render_template("auth.html", register=False, error=error), error.status if error else 200


@bp.route("/verify-email/<token>", methods=["GET", "POST"])
def verify_email(token):
    student_id, email = read_verification_token(token)
    error = None
    if request.method == "POST":
        user = first(
            "SELECT student_id, password_hash FROM Students WHERE student_id = %s AND email = %s AND is_active",
            (student_id, email),
        )
        password = request.form.get("password", "")
        if is_student_email(email) and user and len(password) <= 128 and check_password_hash(user["password_hash"], password):
            write("UPDATE Students SET email_verified = TRUE WHERE student_id = %s", (student_id,))
            return redirect(url_for("accounts.login", verified=1))
        error = "Enter the ExtraCredit password you chose when you registered."
    return render_template("verify_email.html", error=error), 400 if error else 200, {"Referrer-Policy": "no-referrer"}


@bp.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("accounts.login"))


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
        name = text(data, "full_name", 100)
        write("UPDATE Students SET full_name = %s WHERE student_id = %s", (name, student_id))
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
