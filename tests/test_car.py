import sys
import os
import pytest

# Add 'src' to sys.path to import Car
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from entities.car import Car

def test_car_initialization():
    car = Car("Toyota", 15000, 1)
    assert car.name == "Toyota"
    assert car.price == 15000
    assert car.id == 1

def test_car_default_id_none():
    car = Car("Honda", 12000)
    assert car.name == "Honda"
    assert car.price == 12000
    assert car.id is None

def test_car_str_representation_with_id():
    car = Car("BMW", 30000, 7)
    expected = "CAR ID: 7 - NAME: BMW - PRICE: 30000"
    assert str(car) == expected

def test_car_str_representation_without_id():
    car = Car("Mazda", 18000)
    expected = "CAR ID: None - NAME: Mazda - PRICE: 18000"
    assert str(car) == expected