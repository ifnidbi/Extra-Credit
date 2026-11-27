from flask import Blueprint, jsonify

bp = Blueprint("site", __name__)
@bp.route("/")
def home():
    return "Welcome to ExtraCredit!"


@bp.route("/health")
def health():
    return jsonify({"data": {"status": "ok"}})