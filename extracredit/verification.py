from email.message import EmailMessage
from pathlib import Path
import smtplib
from ssl import create_default_context

from flask import current_app, url_for
from itsdangerous import BadSignature, URLSafeTimedSerializer

from .common import AppError


def verification_token(student_id, email):
    signer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt="verify-student-email")
    return signer.dumps([student_id, email])


def read_verification_token(token):
    signer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt="verify-student-email")
    try:
        return signer.loads(token, max_age=86400)
    except BadSignature as error:
        raise AppError(400, "invalid_link", "This confirmation link is invalid or expired.") from error


def send_verification(student_id, email):
    settings = current_app.config
    path = url_for("accounts.verify_email", token=verification_token(student_id, email))
    link = settings["PUBLIC_URL"].rstrip("/") + path
    if settings["DEMO_MODE"]:
        outbox = Path(settings["VERIFICATION_OUTBOX"])
        try:
            outbox.mkdir(mode=0o700, parents=True, exist_ok=True)
            (outbox / f"student-{student_id}.txt").write_text(link + "\n", encoding="utf-8")
        except OSError as error:
            raise AppError(503, "mail_unavailable", "The local confirmation outbox is unavailable.") from error
        return
    if not settings["SMTP_HOST"] or not settings["SMTP_FROM"] or not link.startswith("https://"):
        raise AppError(503, "mail_unavailable", "Account confirmation is unavailable right now.")

    message = EmailMessage()
    message["From"] = settings["SMTP_FROM"]
    message["To"] = email
    message["Subject"] = "Confirm your ExtraCredit account"
    message.set_content(
        "Confirm your Ontario Tech email for ExtraCredit using this link. It expires in 24 hours.\n\n"
        + link + "\n\nIf you did not start this registration, you can ignore this message."
    )
    try:
        with smtplib.SMTP(settings["SMTP_HOST"], settings["SMTP_PORT"], timeout=10) as mail:
            mail.starttls(context=create_default_context())
            if settings["SMTP_USERNAME"]:
                mail.login(settings["SMTP_USERNAME"], settings["SMTP_PASSWORD"])
            mail.send_message(message)
    except (OSError, smtplib.SMTPException) as error:
        current_app.logger.warning("ExtraCredit verification email could not be sent.")
        raise AppError(503, "mail_unavailable", "Account confirmation is unavailable right now.") from error
