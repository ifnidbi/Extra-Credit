from datetime import UTC, date, datetime

from flask import Blueprint, render_template, request

from .accounts import current_user, is_campus_account, require_login
from .campus import CAMPUSES, PICKUP_SPOTS
from .catalog import lock_listing
from .common import AppError, api, form_data, invalid, positive_id, text
from .db import first, rows, transaction, write

bp = Blueprint("inquiries", __name__)
PAYMENT_METHODS = ("Cash", "E-transfer", "Other")
INQUIRY_SQL = """
    SELECT p.inquiry_id, p.listing_id, l.title AS listing_title, l.campus_name, buyer.full_name AS buyer_name,
           seller.full_name AS seller_name, p.pickup_location, p.payment_method,
           p.preferred_date, p.inquiry_status, p.submitted_at,
           CASE WHEN p.buyer_id = %s THEN seller.email ELSE buyer.email END AS other_party_email
    FROM Purchase_Inquiries p
    JOIN Listings l ON l.listing_id = p.listing_id
    JOIN Students buyer ON buyer.student_id = p.buyer_id
    JOIN Students seller ON seller.student_id = l.seller_id
"""


def validate_inquiry(data, campus):
    location = text(data, "pickup_location", 150)
    if location not in PICKUP_SPOTS[campus]:
        invalid("pickup_location", "Choose a pickup spot at the listing's Ontario Tech campus.")
    payment = text(data, "payment_method", 50)
    preferred = text(data, "preferred_date", 10)
    if payment not in PAYMENT_METHODS:
        invalid("payment_method", "Choose a listed payment preference.")
    try:
        day = date.fromisoformat(preferred)
    except ValueError:
        invalid("preferred_date", "Enter a date in YYYY-MM-DD format.")
    if day.isoformat() != preferred or day < datetime.now(UTC).date():
        invalid("preferred_date", "Choose today or a later date.")
    return location, payment, day


def get_inquiry(inquiry_id):
    student_id = current_user()["student_id"]
    item = first(INQUIRY_SQL + " WHERE p.inquiry_id = %s AND (p.buyer_id = %s OR l.seller_id = %s)"
                 " AND l.campus_name IN (%s, %s)", (student_id, inquiry_id, student_id, student_id, *CAMPUSES))
    if not item:
        raise AppError(404, "not_found", "Inquiry not found.")
    return item


def list_inquiries(direction):
    student_id = current_user()["student_id"]
    if direction == "incoming":
        scope = "l.seller_id"
    elif direction == "outgoing":
        scope = "p.buyer_id"
    else:
        invalid("direction", "Choose incoming or outgoing.")
    return rows(INQUIRY_SQL + f" WHERE {scope} = %s AND l.campus_name IN (%s, %s)"
                " ORDER BY p.submitted_at DESC, p.inquiry_id DESC", (student_id, student_id, *CAMPUSES))


def lock_inquiry(inquiry_id, db):
    chosen = first("SELECT listing_id FROM Purchase_Inquiries WHERE inquiry_id = %s", (inquiry_id,), db)
    if not chosen:
        raise AppError(404, "not_found", "Inquiry not found.")
    listing = lock_listing(chosen["listing_id"], db)
    inquiry = first(
        "SELECT buyer_id, inquiry_status FROM Purchase_Inquiries WHERE inquiry_id = %s AND listing_id = %s FOR UPDATE",
        (inquiry_id, listing["listing_id"]), db,
    )
    if not inquiry:
        raise AppError(404, "not_found", "Inquiry not found.")
    return listing, inquiry


def check_pending(inquiry):
    if inquiry["inquiry_status"] != "Pending":
        raise AppError(409, "inquiry_closed", "This inquiry is no longer pending.")


@bp.get("/inquiries")
@require_login
def page():
    direction = request.args.get("direction", "outgoing")
    return render_template("inquiries.html", direction=direction, inquiries=list_inquiries(direction),
                           payment_methods=PAYMENT_METHODS, pickup_spots=PICKUP_SPOTS)


@bp.get("/api/inquiries")
@require_login
def list_api():
    return api(list_inquiries(request.args.get("direction", "outgoing")))


@bp.post("/api/inquiries")
@require_login
def create():
    data = form_data()
    listing_id = positive_id(data.get("listing_id"), "listing_id")
    buyer_id = current_user()["student_id"]
    with transaction() as db:
        listing = lock_listing(listing_id, db)
        if listing["seller_id"] == buyer_id:
            raise AppError(403, "own_listing", "You cannot inquire about your own listing.")
        seller = first("SELECT email, school_name FROM Students WHERE student_id = %s AND is_active AND email_verified",
                       (listing["seller_id"],), db)
        if not is_campus_account(seller) or listing["listing_status"] != "Available":
            raise AppError(409, "listing_unavailable", "This listing is no longer available.")
        values = validate_inquiry(data, listing["campus_name"])
        pending = first(
            """SELECT inquiry_id FROM Purchase_Inquiries
               WHERE listing_id = %s AND buyer_id = %s AND inquiry_status = 'Pending' FOR UPDATE""",
            (listing_id, buyer_id), db,
        )
        if pending:
            raise AppError(409, "duplicate_inquiry", "You already have a pending inquiry for this listing.")
        inquiry_id = write(
            """INSERT INTO Purchase_Inquiries (listing_id, buyer_id, pickup_location, payment_method, preferred_date)
               VALUES (%s,%s,%s,%s,%s)""", (listing_id, buyer_id, *values), db,
        )
    return api(get_inquiry(inquiry_id), 201)


@bp.get("/api/inquiries/<int:inquiry_id>")
@require_login
def detail(inquiry_id):
    return api(get_inquiry(inquiry_id))


@bp.route("/api/inquiries/<int:inquiry_id>", methods=["PUT", "DELETE"])
@require_login
def change(inquiry_id):
    edit = request.method == "PUT"
    with transaction() as db:
        listing, inquiry = lock_inquiry(inquiry_id, db)
        if inquiry["buyer_id"] != current_user()["student_id"]:
            raise AppError(404, "not_found", "Inquiry not found.")
        check_pending(inquiry)
        if edit:
            if listing["listing_status"] != "Available":
                raise AppError(409, "listing_unavailable", "This listing is no longer available.")
            values = validate_inquiry(form_data(), listing["campus_name"])
            write(
                """UPDATE Purchase_Inquiries SET pickup_location = %s, payment_method = %s, preferred_date = %s
                   WHERE inquiry_id = %s""", (*values, inquiry_id), db,
            )
        else:
            write("UPDATE Purchase_Inquiries SET inquiry_status = 'Withdrawn' WHERE inquiry_id = %s", (inquiry_id,), db)
    return api(get_inquiry(inquiry_id)) if edit else ("", 204)


@bp.put("/api/inquiries/<int:inquiry_id>/decision")
@require_login
def decide(inquiry_id):
    decision = form_data().get("decision")
    if decision not in ("Accepted", "Declined"):
        invalid("decision", "Choose Accepted or Declined.")
    with transaction() as db:
        listing, inquiry = lock_inquiry(inquiry_id, db)
        if listing["seller_id"] != current_user()["student_id"]:
            raise AppError(404, "not_found", "Inquiry not found.")
        check_pending(inquiry)
        if decision == "Accepted" and listing["listing_status"] != "Available":
            raise AppError(409, "listing_unavailable", "This listing is no longer available.")
        write("UPDATE Purchase_Inquiries SET inquiry_status = %s WHERE inquiry_id = %s", (decision, inquiry_id), db)
        if decision == "Accepted":
            write("UPDATE Listings SET listing_status = 'Reserved' WHERE listing_id = %s", (listing["listing_id"],), db)
            write(
                """UPDATE Purchase_Inquiries SET inquiry_status = 'Declined'
                   WHERE listing_id = %s AND inquiry_status = 'Pending'""", (listing["listing_id"],), db,
            )
    return api(get_inquiry(inquiry_id))
