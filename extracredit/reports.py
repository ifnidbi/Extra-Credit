import csv
from io import BytesIO, StringIO
from pathlib import Path
from xml.sax.saxutils import escape

import reportlab
from flask import Blueprint, render_template, send_file
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import LongTable, Paragraph, SimpleDocTemplate, TableStyle

from .accounts import require_admin
from .common import AppError, api
from .db import rows

bp = Blueprint("reports", __name__)

REPORTS = {
    "listing-details": ("1. Listing details", "v_listing_details", "listing_id"),
    "seller-price-comparison": ("2. Seller price comparison", "v_seller_price_comparison", "student_id, currency_code"),
    "above-category-average": ("3. Above category average", "v_above_category_average", "listing_id"),
    "listing-inquiry-overview": ("4. Listing and inquiry overview", "v_listing_inquiry_overview", "listing_id, inquiry_id"),
    "active-students": ("5. Students with marketplace activity", "v_active_students", "student_id"),
    "available-listings": ("6. Available listings", "v_available_listings", "currency_code, price, listing_id"),
    "category-summary": ("7. Category summary", "v_category_summary", "category_id, currency_code"),
    "pending-inquiries": ("8. Pending inquiries", "v_pending_inquiries", "inquiry_id"),
    "available-without-images": ("9. Available without images", "v_available_without_images", "listing_id"),
    "student-selling-summary": ("10. Student selling summary", "v_student_selling_summary", "student_id"),
}
CATALOG = ("listing-details", "above-category-average", "available-listings", "category-summary", "available-without-images")
ACTIVITY = ("seller-price-comparison", "listing-inquiry-overview", "active-students", "pending-inquiries", "student-selling-summary")


def get_report(key):
    if key not in REPORTS:
        raise AppError(404, "not_found", "Report not found.")
    title, view, order = REPORTS[key]
    from .db import get_db

    with get_db().cursor(dictionary=True) as cursor:
        cursor.execute(f"SELECT * FROM {view} ORDER BY {order}")
        columns = [{"key": name, "label": name.replace("_", " ").capitalize()} for name in cursor.column_names]
        return {"key": key, "title": title, "columns": columns, "rows": cursor.fetchall()}


@bp.get("/reports/catalog")
@require_admin
def catalog():
    return render_template("reports.html", title="Catalog reports", reports=[get_report(key) for key in CATALOG], chart=True)


@bp.get("/reports/activity")
@require_admin
def activity():
    return render_template("reports.html", title="Activity reports", reports=[get_report(key) for key in ACTIVITY], chart=False)


@bp.get("/api/reports/<key>")
@require_admin
def report_api(key):
    return api(get_report(key))


@bp.get("/api/reports/category-counts")
@require_admin
def category_counts():
    totals = rows(
        """SELECT category_name, SUM(listing_count) AS listing_count FROM v_category_summary
           GROUP BY category_id, category_name ORDER BY category_name"""
    )
    for total in totals:
        total["listing_count"] = int(total["listing_count"])
    return api(totals)


def csv_cell(value):
    if isinstance(value, str) and (value.startswith(("\t", "\r", "\n")) or value.lstrip().startswith(("=", "+", "-", "@", "＝", "＋", "－", "＠"))):
        return "'" + value
    return value


def render_csv(report):
    output = StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow([column["label"] for column in report["columns"]])
    for row in report["rows"]:
        writer.writerow([csv_cell(row[column["key"]]) for column in report["columns"]])
    return BytesIO(output.getvalue().encode("utf-8-sig"))


def render_pdf(report):
    output = BytesIO()
    font = "ExtraCreditVera"
    if font not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont(font, str(Path(reportlab.__file__).parent / "fonts" / "Vera.ttf")))
    style = ParagraphStyle("cell", fontName=font, fontSize=9, leading=12, splitLongWords=True)
    heading = ParagraphStyle("title", parent=style, fontSize=16, leading=20, spaceAfter=12)
    doc = SimpleDocTemplate(output, pagesize=landscape(letter), leftMargin=30, rightMargin=30,
                            topMargin=30, bottomMargin=30, title=report["title"])

    def cell(value):
        value = "—" if value is None else str(value)
        return Paragraph(escape(value), style)

    columns = report["columns"]
    body = [[cell(column["label"]) for column in columns]]
    body += [[cell(row[column["key"]]) for column in columns] for row in report["rows"]]
    table = LongTable(body, repeatRows=1, colWidths=[(doc.width - 12) / len(columns)] * len(columns))
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8eef3")),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.lightgrey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    content = [Paragraph(escape(report["title"]), heading), table]
    if not report["rows"]:
        content.append(Paragraph("No results for this report.", style))
    doc.build(content)
    output.seek(0)
    return output


@bp.get("/api/reports/<key>/export.csv")
@require_admin
def csv_export(key):
    return send_file(render_csv(get_report(key)), "text/csv; charset=utf-8",
                     as_attachment=True, download_name=f"{key}.csv")


@bp.get("/api/reports/<key>/export.pdf")
@require_admin
def pdf_export(key):
    return send_file(render_pdf(get_report(key)), "application/pdf",
                     as_attachment=True, download_name=f"{key}.pdf")
