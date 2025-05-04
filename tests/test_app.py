import sys
import os
import pytest

# Add the 'src' directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# from entities.car import Car
# from entities.car_shop import CarShop
from app import app  # if app.py is the Flask app entry point

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_index(client):
    """Test GET request to '/' route."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"added to the shop" not in response.data  # page renders without POST message

def test_post_add_car(client):
    """Test POST to add a custom car."""
    response = client.post("/", data={
        "add_custom_car": "Add",
        "car_name": "TestCar",
        "car_price": "12345"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"TestCar added to the shop!" in response.data

def test_post_add_car_invalid_price(client):
    """Test POST to add a car with invalid price."""
    response = client.post("/", data={
        "add_custom_car": "Add",
        "car_name": "BadCar",
        "car_price": "notanumber"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid price entered" in response.data

def test_post_remove_car_invalid_id(client):
    """Test POST to remove car with invalid ID."""
    response = client.post("/", data={
        "remove_custom_car": "Remove",
        "car_ID": "invalid_id"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid car ID entered" in response.data