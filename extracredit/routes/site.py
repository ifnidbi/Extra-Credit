from flask import Blueprint, jsonify, redirect, url_for

bp = Blueprint("site", __name__)


@bp.get("/")
def home():
    return redirect(url_for("catalog.index"))


@bp.get("/health")
def health():
    return jsonify({"data": {"status": "ok"}})
