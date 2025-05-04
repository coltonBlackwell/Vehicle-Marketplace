import sys
import os
import pytest

# Add 'src' to sys.path so we can import CarShop
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from entities.car_shop import CarShop
from entities.car import Car

@pytest.fixture(scope="function")
def shop():
    # Create a new CarShop instance (connects to DB)
    cs = CarShop()
    cs.shut_down_store()  # Clean DB before each test
    cs.mycursor.execute("CREATE TABLE IF NOT EXISTS cars (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT)")
    yield cs
    cs.shut_down_store()  # Clean DB after each test

def test_add_car(shop):
    car = Car("TestCar", 9999)
    shop.add_car(car)

    cars = shop.get_all_cars()
    assert len(cars) == 1
    assert cars[0][1] == "TestCar"
    assert cars[0][2] == 9999

def test_remove_car(shop):
    car = Car("DeleteMe", 1000)
    shop.add_car(car)
    car_id = car.id

    shop.remove_car(car_id)

    cars = shop.get_all_cars()
    assert all(c[0] != car_id for c in cars)

def test_get_all_cars(shop):
    car1 = Car("One", 500)
    car2 = Car("Two", 800)
    shop.add_car(car1)
    shop.add_car(car2)

    cars = shop.get_all_cars()
    assert len(cars) == 2
    names = [c[1] for c in cars]
    assert "One" in names and "Two" in names
