class Car:

    def __init__(self, name, price, id=None):
        self.name = name
        self.price = price
        self.id = id

    def __str__(self):
        return f'CAR ID: {self.id} - NAME: {self.name} - PRICE: {self.price}'