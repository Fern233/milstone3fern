
class Inventory:
    def __init__(self,name, base_price, quantity):
        self._name = name
        self._basePrice = base_price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def basePrice(self):
        return self._basePrice

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, added):
        self._quantity = added

    def __str__(self):
        return self._name + " within " + str(self._quantity) + " stores in the inventory has base price " + str(
            self._basePrice) + " dollars."
