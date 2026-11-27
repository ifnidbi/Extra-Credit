from datetime import date
from decimal import Decimal, InvalidOperation

import requests
from flask import Blueprint, render_template

from .accounts import current_user, require_login
from .common import AppError, api, form_data
from .db import first, rows, write

bp = Blueprint("weather", __name__)
PLACE = "Oshawa, Ontario"
LATITUDE = Decimal("43.9001")
LONGITUDE = Decimal("-78.8496")
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


@bp.get("/api/weather/snapshots")
@require_login
def history():
    saved = rows(
        f"""SELECT {FIELDS} FROM Pickup_Forecasts WHERE student_id = %s AND place_label IN (%s, %s)
            ORDER BY fetched_at DESC, snapshot_id DESC LIMIT 10""",
        (current_user()["student_id"], PLACE, PLACE + " (sample)"),
    )
    return api(saved)


@bp.post("/api/weather/snapshots")
@require_login
def save():
    if form_data():
        raise AppError(400, "invalid_place", "Pickup weather uses Oshawa for both Ontario Tech campuses.")
    values = fetch_forecast(LATITUDE, LONGITUDE)
    snapshot_id = write(
        """INSERT INTO Pickup_Forecasts (student_id, place_label, latitude, longitude, forecast_date,
           max_temp_c, precip_probability) VALUES (%s,%s,%s,%s,%s,%s,%s)""",
        (current_user()["student_id"], PLACE, LATITUDE, LONGITUDE, *values),
    )
    return api(first(f"SELECT {FIELDS} FROM Pickup_Forecasts WHERE snapshot_id = %s", (snapshot_id,)), 201)
