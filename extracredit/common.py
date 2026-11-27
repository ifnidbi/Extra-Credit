from flask import jsonify, render_template, request


class AppError(Exception):
    def __init__(self, status, code, message, fields=None):
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message
        self.fields = fields


def api(data, status=200):
    return jsonify({"data": data}), status


def error_response(status, code, message, fields=None):
    if request.path.startswith("/api/") and not request.path.endswith((".pdf", ".csv")):
        error = {"code": code, "message": message}
        if fields:
            error["fields"] = fields
        return jsonify({"error": error}), status
    return render_template("error.html", status=status, message=message), status


def form_data():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        raise AppError(400, "bad_input", "Send a JSON object.")
    return data


def invalid(field, message):
    raise AppError(400, "bad_input", message, {field: message})


def text(data, field, limit, required=True):
    value = data.get(field, "")
    if not isinstance(value, str):
        invalid(field, "Enter text for this field.")
    value = value.strip()
    if not value and required:
        invalid(field, "This field is required.")
    if len(value) > limit:
        invalid(field, f"Use at most {limit} characters.")
    return value


def positive_id(value, field):
    if not str(value).isascii() or not str(value).isdigit() or len(str(value)) > 10:
        invalid(field, "Enter a positive whole number.")
    number = int(value)
    if not 1 <= number <= 4294967295:
        invalid(field, "Enter a positive whole number.")
    return number
