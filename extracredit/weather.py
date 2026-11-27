from datetime import date
from decimal import Decimal, InvalidOperation

import requests
from flask import Blueprint, render_template, request

from .accounts import current_user, require_login
from .common import AppError, api, form_data, invalid, text
from .db import first, rows, write

bp = Blueprint("weather", __name__)
GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST = "https://api.open-meteo.com/v1/forecast"
FIELDS = "snapshot_id, place_label, latitude, longitude, forecast_date, max_temp_c, precip_probability, fetched_at"


def provider_error():
    return AppError(502, "weather_unavailable", "Weather is unavailable right now. Try again shortly.")


def fetch_data(url, params):
    try:
        response = requests.get(url, params=params, timeout=(4, 6))
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError) as error:
        raise provider_error() from error
    if not isinstance(data, dict) or data.get("error"):
        raise provider_error()
    return data


def number(value, minimum, maximum):
    value = Decimal(str(value))
    if not value.is_finite() or not minimum <= value <= maximum:
        raise ValueError("Number is outside its allowed range.")
    return value


def search_places(query):
    if len(query) < 3:
        invalid("q", "Enter at least three characters.")
    data = fetch_data(GEOCODING, {"name": query, "count": 5, "language": "en", "format": "json"})
    try:
        results = data.get("results", [])
        if not isinstance(results, list):
            raise ValueError("Missing place list.")
        places = []
        for item in results[:5]:
            label = ", ".join(dict.fromkeys(item[key] for key in ("name", "admin1", "country") if item.get(key)))
            if not label or len(label) > 150:
                continue
            places.append({
                "place_label": label,
                "latitude": number(item["latitude"], -90, 90),
                "longitude": number(item["longitude"], -180, 180),
            })
        return places
    except (AttributeError, KeyError, TypeError, ValueError, InvalidOperation) as error:
        raise provider_error() from error


def fetch_forecast(latitude, longitude):
    data = fetch_data(FORECAST, {
        "latitude": latitude, "longitude": longitude, "timezone": "auto", "forecast_days": 1,
        "daily": "temperature_2m_max,precipitation_probability_max", "temperature_unit": "celsius",
    })
    try:
        daily = data["daily"]
        day = date.fromisoformat(daily["time"][0])
        temperature = number(daily["temperature_2m_max"][0], -100, 100)
        rain = number(daily["precipitation_probability_max"][0], 0, 100)
        if rain != rain.to_integral_value():
            raise ValueError("Rain probability must be a whole percent.")
        return day, temperature, int(rain)
    except (KeyError, TypeError, IndexError, ValueError, InvalidOperation) as error:
        raise provider_error() from error


@bp.get("/pickup-weather")
@require_login
def page():
    return render_template("weather.html")


@bp.get("/api/weather/places")
@require_login
def places():
    return api(search_places(text(request.args, "q", 100)))


@bp.get("/api/weather/snapshots")
@require_login
def history():
    saved = rows(
        f"""SELECT {FIELDS} FROM Pickup_Forecasts WHERE student_id = %s
            ORDER BY fetched_at DESC, snapshot_id DESC LIMIT 10""",
        (current_user()["student_id"],),
    )
    return api(saved)


@bp.post("/api/weather/snapshots")
@require_login
def save():
    data = form_data()
    label = text(data, "place_label", 150)
    try:
        latitude = number(data.get("latitude"), -90, 90).quantize(Decimal("0.0001"))
        longitude = number(data.get("longitude"), -180, 180).quantize(Decimal("0.0001"))
    except (ValueError, InvalidOperation):
        invalid("coordinates", "Choose a place with valid coordinates.")
    values = fetch_forecast(latitude, longitude)
    snapshot_id = write(
        """INSERT INTO Pickup_Forecasts (student_id, place_label, latitude, longitude, forecast_date,
           max_temp_c, precip_probability) VALUES (%s,%s,%s,%s,%s,%s,%s)""",
        (current_user()["student_id"], label, latitude, longitude, *values),
    )
    return api(first(f"SELECT {FIELDS} FROM Pickup_Forecasts WHERE snapshot_id = %s", (snapshot_id,)), 201)
