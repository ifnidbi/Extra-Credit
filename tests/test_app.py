from datetime import UTC, datetime, timedelta
from io import BytesIO
import csv

import pytest
import requests
from PIL import Image
from pypdf import PdfReader

from extracredit import create_app, inquiries, weather
from extracredit.db import first, rows, write
from extracredit.reports import REPORTS, render_pdf

from conftest import DEMO_PASSWORD, csrf_token

LISTING = {
    "title": "Campus lamp", "description": "Works well", "campus_name": "Lakeview College",
    "price": "19.25", "currency_code": "CAD", "item_condition": "Good", "category_id": "2",
}


def pickup(listing_id):
    return {
        "listing_id": listing_id, "pickup_location": "Library entrance", "payment_method": "Cash",
        "preferred_date": (datetime.now(UTC).date() + timedelta(days=2)).isoformat(),
    }


def test_health_without_a_database():
    app = create_app({"TESTING": True, "DB_PORT": 1})
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json == {"data": {"status": "ok"}}


def test_database_failure_has_readable_html_and_json():
    app = create_app({"TESTING": True, "DB_PORT": 1})
    client = app.test_client()
    assert client.get("/listings").status_code == 503
    response = client.get("/api/listings")
    assert response.status_code == 503
    assert response.json["error"]["code"] == "database_unavailable"


def test_demo_seed_has_six_rows_per_table(app):
    tables = ("Students", "Categories", "Listings", "Listing_Images", "Purchase_Inquiries", "Pickup_Forecasts")
    with app.app_context():
        for table in tables:
            assert first(f"SELECT COUNT(*) AS total FROM {table}")["total"] >= 6, table
        forecasts = rows("SELECT place_label FROM Pickup_Forecasts")
    assert all(row["place_label"].endswith("(sample)") for row in forecasts)


def test_registration_is_open_to_multiple_schools(app, api_write):
    client = app.test_client()
    for address in (" TESS@college.example.org ", "lee@institute.example.net"):
        response = client.post("/register", data={
            "full_name": "Test name", "school_name": "Test School", "email": address,
            "password": DEMO_PASSWORD, "student_attested": "yes", "role": "admin", "csrf_token": csrf_token(client),
        })
        assert response.status_code == 302
    with app.app_context():
        new = first("SELECT email, role, password_hash FROM Students WHERE email = 'tess@college.example.org'")
    assert new["email"] == "tess@college.example.org"
    assert new["role"] == "user"
    assert new["password_hash"] != DEMO_PASSWORD
    response = client.post("/register", data={
        "full_name": "Test name", "school_name": "Test School", "email": "tess@college.example.org",
        "password": DEMO_PASSWORD, "student_attested": "yes", "csrf_token": csrf_token(client),
    })
    assert response.status_code == 409
    invalid = client.post("/register", data={
        "full_name": "Test name", "school_name": "Test School", "email": "bad email",
        "password": DEMO_PASSWORD, "csrf_token": csrf_token(client),
    })
    assert invalid.status_code == 400
    assert DEMO_PASSWORD not in invalid.get_data(as_text=True)


def test_session_profile_permissions_and_csrf(app, sign_in, api_write):
    client = sign_in("alex")
    assert client.get("/api/account").json["data"]["role"] == "user"
    assert client.get("/reports/catalog").status_code == 403
    assert client.get("/api/reports/listing-details").status_code == 403
    assert client.put("/api/account", json={"full_name": "Alex", "school_name": "Lakeview"}).status_code == 400
    assert api_write(client, "PUT", "/api/account", {"full_name": "Alex M.", "school_name": "Lakeview"}).status_code == 200
    assert client.get("/api/account").json["data"]["full_name"] == "Alex M."
    assert client.get("/logout").status_code == 405
    assert client.post("/logout", data={"csrf_token": csrf_token(client)}).status_code == 302
    assert client.get("/api/account").status_code == 401


def test_deactivate_keeps_history_and_hides_public_listings(app, sign_in, api_write):
    client = sign_in("alex")
    assert api_write(client, "DELETE", "/api/account", {"password": "bad"}).status_code == 400
    assert api_write(client, "DELETE", "/api/account", {"password": DEMO_PASSWORD}).status_code == 204
    assert client.get("/api/account").status_code == 401
    assert client.get("/api/listings/6").status_code == 404
    assert client.post("/login", data={"email": "alex@example.com", "password": DEMO_PASSWORD,
                                     "csrf_token": csrf_token(client)}).status_code == 401
    with app.app_context():
        assert first("SELECT listing_id FROM Listings WHERE listing_id = 6") is not None


def test_listing_crud_filter_and_public_fields(app, sign_in, api_write):
    owner, other = sign_in("alex"), sign_in("priya")
    created = api_write(owner, "POST", "/api/listings", LISTING | {"seller_id": 2, "listing_status": "Sold"})
    assert created.status_code == 201
    listing = created.json["data"]
    assert listing["listing_status"] == "Available" and listing["seller_name"] == "Alex Morgan"
    url = f"/api/listings/{listing['listing_id']}"
    assert api_write(other, "PUT", url, LISTING).status_code == 403
    assert api_write(owner, "PUT", url, LISTING | {"price": "Infinity"}).status_code == 400
    assert app.test_client().get(url).json["data"]["price"] == "19.25"
    assert "email" not in app.test_client().get(url).json["data"]
    assert api_write(owner, "PUT", url, LISTING | {"price": "23.00"}).json["data"]["price"] == "23.00"
    assert api_write(owner, "DELETE", url).status_code == 204
    assert app.test_client().get(url).status_code == 404
    assert owner.get(url).json["data"]["listing_status"] == "Removed"

    guest = app.test_client()
    results = guest.get("/api/listings?campus=Lakeview&currency=CAD&min_price=40&max_price=50").json["data"]["items"]
    assert [item["listing_id"] for item in results] == [1]
    assert guest.get("/api/listings?q=%25").json["data"]["items"] == []
    assert guest.get("/api/listings?min_price=5").status_code == 400
    assert guest.get("/api/listings/5").status_code == 404
    assert guest.get("/listings?page=2").status_code == 200


def test_sold_listing_declines_pending_inquiries(app, sign_in, api_write):
    seller = sign_in("alex")
    response = api_write(seller, "PUT", "/api/listings/1/status", {"listing_status": "Sold"})
    assert response.json["data"]["listing_status"] == "Sold"
    assert api_write(seller, "PUT", "/api/listings/1/status", {"listing_status": "Sold"}).status_code == 409
    with app.app_context():
        assert {row["inquiry_status"] for row in rows("SELECT inquiry_status FROM Purchase_Inquiries WHERE listing_id = 1")} == {"Declined"}


def test_category_admin_can_crud_but_cannot_delete_in_use(sign_in, api_write):
    admin = sign_in("admin")
    student = sign_in("alex")
    assert api_write(student, "POST", "/api/categories", {"category_name": "Games"}).status_code == 403
    response = api_write(admin, "POST", "/api/categories", {"category_name": "Games"})
    assert response.status_code == 201
    url = f"/api/categories/{response.json['data']['category_id']}"
    assert api_write(admin, "PUT", url, {"category_name": "Board Games"}).status_code == 200
    assert api_write(admin, "DELETE", "/api/categories/1").status_code == 409
    assert api_write(admin, "DELETE", url).status_code == 204
    assert admin.get("/admin/categories").status_code == 200


def test_inquiries_are_private_and_can_be_changed(app, sign_in, api_write):
    buyer, seller, other = sign_in("priya"), sign_in("alex"), sign_in("maya")
    assert api_write(seller, "POST", "/api/inquiries", pickup(1)).status_code == 403
    assert api_write(buyer, "POST", "/api/inquiries", pickup(1)).status_code == 409
    created = api_write(buyer, "POST", "/api/inquiries", pickup(8))
    assert created.status_code == 201
    url = f"/api/inquiries/{created.json['data']['inquiry_id']}"
    assert other.get(url).status_code == 404
    assert buyer.get(url).json["data"]["other_party_email"] == "jordan@example.com"
    assert api_write(buyer, "PUT", url, pickup(8) | {"pickup_location": "Cafe"}).json["data"]["pickup_location"] == "Cafe"
    assert api_write(buyer, "DELETE", url).status_code == 204
    assert buyer.get(url).json["data"]["inquiry_status"] == "Withdrawn"
    assert buyer.get("/inquiries?direction=outgoing").status_code == 200


def test_acceptance_reserves_listing_and_rolls_back_on_failure(app, sign_in, api_write, monkeypatch):
    seller = sign_in("alex")
    real_write = inquiries.write

    def fail_reservation(sql, values=(), db=None):
        if "UPDATE Listings" in sql:
            raise RuntimeError("test failure")
        return real_write(sql, values, db)

    with monkeypatch.context() as patch:
        patch.setattr(inquiries, "write", fail_reservation)
        with pytest.raises(RuntimeError, match="test failure"):
            api_write(seller, "PUT", "/api/inquiries/1/decision", {"decision": "Accepted"})

    assert seller.get("/api/inquiries/1").json["data"]["inquiry_status"] == "Pending"
    assert seller.get("/api/listings/1").json["data"]["listing_status"] == "Available"
    accepted = api_write(seller, "PUT", "/api/inquiries/1/decision", {"decision": "Accepted"})
    assert accepted.json["data"]["inquiry_status"] == "Accepted"
    assert seller.get("/api/inquiries/2").json["data"]["inquiry_status"] == "Declined"
    assert seller.get("/api/listings/1").json["data"]["listing_status"] == "Reserved"
    assert api_write(seller, "PUT", "/api/inquiries/1/decision", {"decision": "Accepted"}).status_code == 409


def test_photo_upload_link_access_and_removal(app, sign_in, api_write):
    owner, other = sign_in("alex"), sign_in("priya")

    def upload(client, content):
        return api_write(client, "POST", "/api/listings/1/images", data={"photo": (BytesIO(content), "test.png")},
                         content_type="multipart/form-data")

    output = BytesIO()
    Image.new("RGB", (24, 18), "blue").save(output, "PNG")
    content = output.getvalue()
    response = upload(owner, content)
    assert response.status_code == 201
    photo = response.json["data"]
    directory = app.config["UPLOAD_DIR"]
    assert len(list(directory.iterdir())) == 1
    guest = app.test_client()
    assert guest.get(photo["media_url"]).content_type == "image/png"
    assert guest.get(f"/media/listings/6/{photo['image_id']}").status_code == 404
    assert upload(owner, b"plain text").status_code == 400
    assert upload(other, content).status_code == 403
    assert api_write(owner, "DELETE", f"/api/listings/1/images/{photo['image_id']}").status_code == 204
    assert guest.get(photo["media_url"]).status_code == 404
    assert list(directory.iterdir()) == []


def test_views_report_pages_chart_and_exports(app, sign_in):
    admin = sign_in("admin")
    assert admin.get("/api/reports/unknown").status_code == 404
    pages = [admin.get("/reports/catalog"), admin.get("/reports/activity")]
    assert all(page.status_code == 200 for page in pages)
    assert sum(page.get_data(as_text=True).count("<table") for page in pages) == 10
    for key, (title, view, order) in REPORTS.items():
        payload = admin.get(f"/api/reports/{key}").json["data"]
        with app.app_context():
            expected = rows(f"SELECT * FROM {view} ORDER BY {order}")
        assert payload["title"] == title
        assert payload["rows"] == app.json.loads(app.json.dumps(expected))
        assert payload["rows"], key
    totals = {row["category_name"]: row["listing_count"]
              for row in admin.get("/api/reports/category-counts").json["data"]}
    assert totals["School Supplies"] == 0 and totals["Textbooks"] == 3
    with app.app_context():
        write("UPDATE Listings SET title = %s WHERE listing_id = 1", ('=1+1, "sample"',))
    csv_response = admin.get("/api/reports/listing-details/export.csv")
    csv_rows = list(csv.reader(csv_response.data.decode("utf-8-sig").splitlines()))
    assert csv_rows[1][1] == "'=1+1, \"sample\""
    pdf_response = admin.get("/api/reports/listing-details/export.pdf")
    assert pdf_response.status_code == 200
    assert "Listing details" in PdfReader(BytesIO(pdf_response.data)).pages[0].extract_text()


def test_pdf_headers_repeat_on_page_breaks():
    report = {
        "title": "Test report", "columns": [{"key": "title", "label": "Title"}],
        "rows": [{"title": "Sample < & > " * 23} for _ in range(100)],
    }
    pdf = PdfReader(render_pdf(report))
    assert len(pdf.pages) > 1
    assert "Title" in pdf.pages[-1].extract_text()
    assert "< & >" in pdf.pages[-1].extract_text()


def test_weather_saves_results_and_scopes_history(app, sign_in, api_write, monkeypatch):
    student, other = sign_in("alex"), sign_in("priya")

    class FakeResponse:
        def __init__(self, data):
            self.value = data

        def raise_for_status(self):
            pass

        def json(self):
            return self.value

    def fake_get(url, params, timeout):
        if url == weather.GEOCODING:
            return FakeResponse({"results": [{"name": "Toronto", "country": "Canada", "latitude": 43.7, "longitude": -79.4}]})
        assert params["timezone"] == "auto"
        return FakeResponse({"daily": {"time": ["2026-11-26"], "temperature_2m_max": [3.8],
                                       "precipitation_probability_max": [8]}})

    monkeypatch.setattr(weather.requests, "get", fake_get)
    place = student.get("/api/weather/places?q=Toronto").json["data"][0]
    saved = api_write(student, "POST", "/api/weather/snapshots", place)
    assert saved.status_code == 201
    assert saved.json["data"]["forecast_date"] == "2026-11-26"
    assert student.get("/api/weather/snapshots").json["data"] == [saved.json["data"]]
    assert other.get("/api/weather/snapshots").json["data"] == []
    assert api_write(student, "POST", "/api/weather/snapshots", place | {"latitude": "NaN"}).status_code == 400

    def timeout(*args, **kwargs):
        raise requests.Timeout()

    monkeypatch.setattr(weather.requests, "get", timeout)
    assert api_write(student, "POST", "/api/weather/snapshots", place).status_code == 502
    assert len(student.get("/api/weather/snapshots").json["data"]) == 1
