import requests
import pytest

@pytest.fixture()
def username_password_data():
    data = {
        "username": "admin",
        "password": "password123"
    }
    return data
@pytest.fixture()
def booking_data():
    data = {
        "firstname": "Osachi",
        "lastname": "Roman",
        "totalprice": 999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2019-01-01",
            "checkout": "2019-01-02"
        },
        "additionalneeds": "kats"
    }
    return data
