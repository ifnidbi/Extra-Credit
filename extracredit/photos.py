from io import BytesIO
from pathlib import Path
from uuid import uuid4

from flask import Blueprint, current_app, request, send_from_directory, url_for
from PIL import Image, ImageOps, UnidentifiedImageError

from .accounts import require_login
from .catalog import check_editable, check_owner, get_listing, lock_listing
from .common import AppError, api, invalid
from .db import first, rows, transaction, write

bp = Blueprint("photos", __name__)
PHOTO_LIMIT = 3 * 1024 * 1024


def upload_dir():
    return Path(current_app.config["UPLOAD_DIR"])


def validate_photo(upload):
    if not upload:
        invalid("photo", "Choose a JPEG or PNG photo.")
    data = upload.stream.read(PHOTO_LIMIT + 1)
    if len(data) > PHOTO_LIMIT:
        raise AppError(413, "photo_too_large", "Choose a photo under 3 MiB.")
    try:
        with Image.open(BytesIO(data), formats=("JPEG", "PNG")) as image:
            if image.width > 4000 or image.height > 4000 or getattr(image, "is_animated", False):
                invalid("photo", "Choose a still photo up to 4000 by 4000 pixels.")
            kind = image.format
            mode = "RGB" if kind == "JPEG" else "RGBA"
            upright = ImageOps.exif_transpose(image)
            clean = Image.new(mode, upright.size)
            clean.paste(upright.convert(mode))
            output = BytesIO()
            clean.save(output, format=kind)
    except (UnidentifiedImageError, OSError, ValueError, Image.DecompressionBombError):
        invalid("photo", "Choose a readable JPEG or PNG photo.")
    if output.tell() > PHOTO_LIMIT:
        raise AppError(413, "photo_too_large", "Choose a smaller photo.")
    return output.getvalue(), "jpg" if kind == "JPEG" else "png"


def listing_photos(listing_id):
    photos = rows("SELECT image_id, image_path FROM Listing_Images WHERE listing_id = %s ORDER BY image_id", (listing_id,))
    for photo in photos:
        photo["media_url"] = url_for("photos.media", listing_id=listing_id, image_id=photo["image_id"])
        photo["exists"] = (upload_dir() / photo["image_path"]).is_file()
    return photos


def remove_file(path):
    try:
        path.unlink(missing_ok=True)
    except OSError:
        current_app.logger.warning("Could not remove a stored photo.")


@bp.post("/api/listings/<int:listing_id>/images")
@require_login
def upload(listing_id):
    get_listing(listing_id)
    content, extension = validate_photo(request.files.get("photo"))
    name = f"{uuid4().hex}.{extension}"
    path = upload_dir() / name
    saved = False
    try:
        with transaction() as db:
            listing = lock_listing(listing_id, db)
            check_owner(listing)
            check_editable(listing)
            count = first("SELECT COUNT(*) AS total FROM Listing_Images WHERE listing_id = %s", (listing_id,), db)
            if count["total"] >= 5:
                raise AppError(409, "photo_limit", "Each listing can have up to five photos.")
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as file:
                saved = True
                file.write(content)
            image_id = write("INSERT INTO Listing_Images (listing_id, image_path) VALUES (%s,%s)", (listing_id, name), db)
    except Exception:
        if saved:
            remove_file(path)
        raise
    return api({"image_id": image_id, "media_url": url_for("photos.media", listing_id=listing_id, image_id=image_id)}, 201)


def photo_row(listing_id, image_id, db=None):
    photo = first("SELECT image_path FROM Listing_Images WHERE listing_id = %s AND image_id = %s",
                  (listing_id, image_id), db)
    if not photo or photo["image_path"] != Path(photo["image_path"]).name:
        raise AppError(404, "not_found", "Photo not found.")
    return photo


@bp.get("/media/listings/<int:listing_id>/<int:image_id>")
def media(listing_id, image_id):
    get_listing(listing_id)
    photo = photo_row(listing_id, image_id)
    return send_from_directory(upload_dir().resolve(), photo["image_path"], max_age=0)


@bp.delete("/api/listings/<int:listing_id>/images/<int:image_id>")
@require_login
def remove(listing_id, image_id):
    with transaction() as db:
        listing = lock_listing(listing_id, db)
        check_owner(listing)
        check_editable(listing)
        photo = photo_row(listing_id, image_id, db)
        write("DELETE FROM Listing_Images WHERE image_id = %s", (image_id,), db)
    remove_file(upload_dir() / photo["image_path"])
    return "", 204
