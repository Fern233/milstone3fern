from abc import ABC
from error import orderError
from error import makeOrderError1
from error import makeOrderError2
from error import makeOrderError3

class Main(ABC):
    def __init__(self):
        self._ingredient = []
        self._patties = []

    def calculatePrice(self):
        total = 0
        for key in self._ingredient:
            total += key.quantity*key.price

        for patty in self._patties:
            total += patty.quantity*patty.price

        return total

    def addIngredient(self, ingredient):
        self._ingredient.append(ingredient)

    def addPatties(self, patties):
        try:
            makeOrderError3(patties)
        except orderError as e:
            return e
        else:
            self._patties.append(patties)

    def __str__(self):
        output = ''

        for key in self._ingredient:
            output += f'{key.quantity} {key.name}'

        return output

    @property
    def ingredient(self):
        return self._ingredient


class Burger(Main):
    def __init__(self):
        super().__init__()
        self._buns = []

    def calculatePrice(self):
        total = super().calculatePrice()

        for bun in self._buns:
            total += bun.price*bun.quantity

        return total

    def __str__(self):
        output = 'you have ordered a burger within '
        for key in self._buns:
            output += f' {key.quantity} {key.name} '

        return output + super().__str__()

    def addBuns(self,buns):
        try:
            makeOrderError1(buns)
        except orderError as e:
            return e
        else:
            self._buns.append(buns)

    @property
    def buns(self):
        return self._buns


class Wrap(Main):
    def __init__(self):
        super().__init__()
        self._wraps = []


    def calculatePrice(self):
        total = super().calculatePrice()

        for bun in self._wraps:
            total += bun.price * bun.quantity

        return total
    def __str__(self):
        output = 'you have ordered a wrap within'

        for key in self._wraps:
            output += f' {key.quantity} {key.name} '

        return output + super().__str__()


    def addWrap(self,wrap):
        try:
            makeOrderError2(wrap)
        except orderError as e:
            return e
        else:
            self._wraps.append(wrap)

    @property
    def wraps(self):
        return self._wraps


class Extra():

    def __init__(self):
        self._ingredient = []

    def calculatePrice(self):
        total = 0
        for key in self._ingredient:
            total += key.quantity * key.price

        return total

    def addExtra(self, ingredient):
        self._ingredient.append(ingredient)

    def __str__(self):
        output = ''

        for key in self._ingredient:
            output += f'{key.quantity} {key.name}'

        return output
    @property
    def ingredient(self):
        return self._ingredient