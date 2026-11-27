from decimal import Decimal, InvalidOperation

from flask import Blueprint, current_app, render_template, request
from mysql.connector import IntegrityError

from .accounts import current_user, require_admin, require_login
from .campus import CAMPUSES, DEMO_EMAILS, PICKUP_SPOTS, SCHOOL, STUDENT_DOMAIN
from .common import AppError, api, form_data, invalid, positive_id, text
from .db import first, rows, transaction, write

bp = Blueprint("catalog", __name__)
CONDITIONS = ("New", "Like New", "Good", "Fair", "Poor")
CURRENCIES = ("CAD", "USD", "EUR", "GBP", "JPY")
EDITABLE = ("Available", "Reserved")
PAGE_SIZE = 50

LISTING_SQL = """
    SELECT l.listing_id, l.title, l.description, l.category_id, c.category_name,
           l.campus_name, l.price, l.currency_code, l.item_condition, l.listing_status,
           l.date_posted, l.seller_id, s.full_name AS seller_name, s.is_active AS seller_active
    FROM Listings l JOIN Students s ON s.student_id = l.seller_id
    JOIN Categories c ON c.category_id = l.category_id
"""
SELLER_SCOPE = "s.email_verified AND s.school_name = %s"


def allowed_seller():
    sql = SELLER_SCOPE + " AND (SUBSTRING_INDEX(s.email, '@', -1) = %s"
    values = [SCHOOL, STUDENT_DOMAIN]
    if current_app.config["DEMO_MODE"]:
        sql += " OR s.email IN (" + ",".join(["%s"] * len(DEMO_EMAILS)) + ")"
        values.extend(DEMO_EMAILS)
    return sql + ")", values


def list_categories():
    return rows("SELECT category_id, category_name FROM Categories ORDER BY category_name")


def price_value(value, currency, field):
    try:
        amount = Decimal(str(value))
    except InvalidOperation:
        invalid(field, "Enter a valid price.")
    if not amount.is_finite() or not 0 <= amount <= Decimal("99999999.99"):
        invalid(field, "Enter a price from 0 to 99,999,999.99.")
    if amount.as_tuple().exponent < -2 or (currency == "JPY" and amount != amount.to_integral_value()):
        invalid(field, "Use at most two decimal places and no fractions for JPY.")
    return amount


def like_value(value):
    return "%" + value.replace("!", "!!").replace("%", "!%").replace("_", "!_") + "%"


def search_listings(args):
    q = text(args, "q", 150, required=False)
    campus = text(args, "campus", 150, required=False)
    currency = args.get("currency", "")
    condition = args.get("condition", "")
    page = positive_id(args.get("page", 1), "page")
    if currency and currency not in CURRENCIES:
        invalid("currency", "Choose a listed currency.")
    if condition and condition not in CONDITIONS:
        invalid("condition", "Choose a listed condition.")
    if campus and campus not in CAMPUSES:
        invalid("campus", "Choose North Oshawa or Downtown Oshawa.")

    scope, values = allowed_seller()
    filters = ["l.listing_status = 'Available'", "s.is_active", scope, "l.campus_name IN (%s, %s)"]
    values.extend(CAMPUSES)
    if q:
        filters.append("(l.title LIKE %s ESCAPE '!' OR l.description LIKE %s ESCAPE '!')")
        values.extend((like_value(q), like_value(q)))
    if campus:
        filters.append("l.campus_name = %s")
        values.append(campus)
    if args.get("category_id"):
        filters.append("l.category_id = %s")
        values.append(positive_id(args["category_id"], "category_id"))
    if currency:
        filters.append("l.currency_code = %s")
        values.append(currency)
    if condition:
        filters.append("l.item_condition = %s")
        values.append(condition)
    prices = {}
    for field, operator in (("min_price", ">="), ("max_price", "<=")):
        if args.get(field):
            if not currency:
                invalid("currency", "Choose a currency to search by price.")
            prices[field] = price_value(args[field], currency, field)
            filters.append(f"l.price {operator} %s")
            values.append(prices[field])
    if len(prices) == 2 and prices["min_price"] > prices["max_price"]:
        invalid("max_price", "The maximum price must be at least the minimum.")
    values.extend((PAGE_SIZE + 1, (page - 1) * PAGE_SIZE))
    sql = LISTING_SQL + " WHERE " + " AND ".join(filters)
    matches = rows(sql + " ORDER BY l.date_posted DESC, l.listing_id DESC LIMIT %s OFFSET %s", tuple(values))
    return {"items": matches[:PAGE_SIZE], "page": page, "has_next": len(matches) > PAGE_SIZE}


def get_listing(listing_id):
    scope, values = allowed_seller()
    listing = first(LISTING_SQL + f" WHERE l.listing_id = %s AND l.campus_name IN (%s, %s) AND {scope}",
                    (listing_id, *CAMPUSES, *values))
    user = current_user()
    privileged = listing and user and (listing["seller_id"] == user["student_id"] or user["role"] == "admin")
    if not listing or ((not listing["seller_active"] or listing["listing_status"] == "Removed") and not privileged):
        raise AppError(404, "not_found", "Listing not found.")
    return listing


def public_listing(listing):
    return {key: value for key, value in listing.items() if key not in ("seller_id", "seller_active")}


def validate_listing(data):
    currency = text(data, "currency_code", 3)
    condition = text(data, "item_condition", 20)
    campus = text(data, "campus_name", 150)
    if campus not in CAMPUSES:
        invalid("campus_name", "Choose an Ontario Tech campus.")
    if currency not in CURRENCIES:
        invalid("currency_code", "Choose a listed currency.")
    if condition not in CONDITIONS:
        invalid("item_condition", "Choose a listed condition.")
    category_id = positive_id(data.get("category_id"), "category_id")
    if not first("SELECT category_id FROM Categories WHERE category_id = %s", (category_id,)):
        invalid("category_id", "Choose an existing category.")
    return (
        text(data, "title", 150), text(data, "description", 5000, required=False),
        price_value(data.get("price"), currency, "price"), currency, condition,
        category_id, campus,
    )


def lock_listing(listing_id, db):
    listing = first(
        "SELECT listing_id, seller_id, listing_status, campus_name FROM Listings WHERE listing_id = %s FOR UPDATE",
        (listing_id,), db,
    )
    if not listing or listing["campus_name"] not in CAMPUSES:
        raise AppError(404, "not_found", "Listing not found.")
    return listing


def check_owner(listing, admin_can_remove=False):
    user = current_user()
    if user["student_id"] != listing["seller_id"] and not (admin_can_remove and user["role"] == "admin"):
        raise AppError(403, "forbidden", "Only the seller can change this listing.")


def check_editable(listing):
    if listing["listing_status"] not in EDITABLE:
        raise AppError(409, "listing_closed", "Only available or reserved listings can be edited.")


@bp.get("/listings")
@require_login
def index():
    return render_template("listings.html", result=search_listings(request.args), categories=list_categories(),
                           currencies=CURRENCIES, conditions=CONDITIONS, campuses=CAMPUSES)


@bp.get("/listings/<int:listing_id>")
@require_login
def detail(listing_id):
    from .photos import listing_photos

    listing = get_listing(listing_id)
    return render_template("listing.html", listing=listing, photos=listing_photos(listing_id),
                           pickup_spots=PICKUP_SPOTS[listing["campus_name"]])


@bp.get("/dashboard")
@require_login
def dashboard():
    listings = rows(LISTING_SQL + " WHERE l.seller_id = %s AND l.campus_name IN (%s, %s)"
                    " ORDER BY l.date_posted DESC, l.listing_id DESC",
                    (current_user()["student_id"], *CAMPUSES))
    return render_template("dashboard.html", listings=listings)


@bp.get("/listings/new")
@bp.get("/listings/<int:listing_id>/edit")
@require_login
def editor(listing_id=None):
    from .photos import listing_photos

    listing = get_listing(listing_id) if listing_id is not None else None
    if listing:
        check_owner(listing)
        check_editable(listing)
    return render_template("editor.html", listing=listing, categories=list_categories(), currencies=CURRENCIES,
                           conditions=CONDITIONS, campuses=CAMPUSES,
                           photos=listing_photos(listing_id) if listing else [])


@bp.get("/api/listings")
@require_login
def search_api():
    result = search_listings(request.args)
    result["items"] = [public_listing(item) for item in result["items"]]
    return api(result)


@bp.get("/api/listings/<int:listing_id>")
@require_login
def detail_api(listing_id):
    return api(public_listing(get_listing(listing_id)))


@bp.post("/api/listings")
@require_login
def create_listing():
    values = validate_listing(form_data())
    try:
        listing_id = write(
            """INSERT INTO Listings (title, description, price, currency_code, item_condition,
                       category_id, campus_name, seller_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
            (*values, current_user()["student_id"]),
        )
    except IntegrityError as error:
        if error.errno != 1452:
            raise
        raise AppError(409, "category_changed", "The category is no longer available.") from error
    return api(public_listing(get_listing(listing_id)), 201)


@bp.put("/api/listings/<int:listing_id>")
@require_login
def update_listing(listing_id):
    values = validate_listing(form_data())
    try:
        with transaction() as db:
            listing = lock_listing(listing_id, db)
            check_owner(listing)
            check_editable(listing)
            if values[-1] != listing["campus_name"] and first(
                "SELECT inquiry_id FROM Purchase_Inquiries WHERE listing_id = %s "
                "AND inquiry_status IN ('Pending', 'Accepted') LIMIT 1 FOR UPDATE", (listing_id,), db,
            ):
                raise AppError(409, "pickup_pending", "The campus cannot change while a pickup is pending or accepted.")
            write(
                """UPDATE Listings SET title=%s, description=%s, price=%s, currency_code=%s,
                   item_condition=%s, category_id=%s, campus_name=%s WHERE listing_id=%s""",
                (*values, listing_id), db,
            )
    except IntegrityError as error:
        if error.errno != 1452:
            raise
        raise AppError(409, "category_changed", "The category is no longer available.") from error
    return api(public_listing(get_listing(listing_id)))


def close_listing(listing_id, status):
    with transaction() as db:
        listing = lock_listing(listing_id, db)
        check_owner(listing, admin_can_remove=status == "Removed")
        if status == "Sold":
            check_editable(listing)
        if listing["listing_status"] == "Removed":
            raise AppError(409, "listing_closed", "This listing was already removed.")
        write("UPDATE Listings SET listing_status = %s WHERE listing_id = %s", (status, listing_id), db)
        write(
            "UPDATE Purchase_Inquiries SET inquiry_status = 'Declined' WHERE listing_id = %s AND inquiry_status = 'Pending'",
            (listing_id,), db,
        )


@bp.put("/api/listings/<int:listing_id>/status")
@require_login
def sell_listing(listing_id):
    if form_data().get("listing_status") != "Sold":
        invalid("listing_status", "Choose Sold.")
    close_listing(listing_id, "Sold")
    return api(public_listing(get_listing(listing_id)))


@bp.delete("/api/listings/<int:listing_id>")
@require_login
def remove_listing(listing_id):
    close_listing(listing_id, "Removed")
    return "", 204


@bp.get("/admin/categories")
@require_admin
def categories_page():
    return render_template("categories.html", categories=list_categories())


@bp.get("/api/categories")
@require_login
def categories_api():
    return api(list_categories())


@bp.post("/api/categories")
@bp.route("/api/categories/<int:category_id>", methods=["PUT", "DELETE"])
@require_admin
def change_category(category_id=None):
    method = request.method
    if method != "DELETE":
        name = text(form_data(), "category_name", 100)
    try:
        with transaction() as db:
            if category_id is not None and not first(
                "SELECT category_id FROM Categories WHERE category_id = %s FOR UPDATE", (category_id,), db
            ):
                raise AppError(404, "not_found", "Category not found.")
            if method == "POST":
                category_id = write("INSERT INTO Categories (category_name) VALUES (%s)", (name,), db)
            elif method == "PUT":
                write("UPDATE Categories SET category_name = %s WHERE category_id = %s", (name, category_id), db)
            else:
                write("DELETE FROM Categories WHERE category_id = %s", (category_id,), db)
    except IntegrityError as error:
        if error.errno == 1062:
            raise AppError(409, "duplicate_category", "That category already exists.") from error
        if error.errno == 1451:
            raise AppError(409, "category_in_use", "A listing still uses this category.") from error
        raise
    if method == "DELETE":
        return "", 204
    return api({"category_id": category_id, "category_name": name}, 201 if method == "POST" else 200)
