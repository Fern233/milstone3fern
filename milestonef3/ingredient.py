class Ingredient():

    def __init__(self, name, price, quantity):
        self._name = name
        self._quantity = quantity
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price
