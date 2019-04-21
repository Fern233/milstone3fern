class Order():

    def __init__(self,status,orderID):
        self._mainfoods = []
        self._extrafoods = []
        self._status = status
        self._orderID = orderID
        self.reduce = 'not' ##############


    def addMain(self,main):
        self._mainfoods.append(main)

    def addExtra(self,extra):
        self._extrafoods.append(extra)

    def totalPrice(self):
        Price1 = 0
        Price2 = 0

        for main in self._mainfoods:
            Price1 += main.calculatePrice()

        for extra in self._extrafoods:
            Price2 += extra.calculatePrice()

        totalPrice = Price1 + Price2
        return totalPrice

    def __str__(self):
        output = ''
        output += f'orderID: {self._orderID}\n'
        output += f'you have ordered {len(self._mainfoods)} main '
        output += f'and {len(self._extrafoods)} extra\n'
        output += f'total price is {self.totalPrice():.2f}'
        return output

    @property
    def mainFoods(self):
        return self._mainfoods

    @property
    def extraFoods(self):
        return self._extrafoods

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new):
        self._status = new

    @property
    def orderID(self):
        return self._orderID