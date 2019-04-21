from order import Order
from error import ourofstockError4
from error import orderError
import random
class System():

    def __init__(self):
        self._stock = []
        self._orders = []

    def addStock(self,stock):
        self._stock.append(stock)

    def deleteStock(self,name):
        for inventory in self._stock:
            if inventory.name == name:
                self._stock.remove(inventory)

    def refillStock(self, name, quantity):
        for inventory in self._stock:
            if name == inventory.name:
                inventory.quantity += quantity

    def reduceStock(self, whatOrdered):
        for inventory in self._stock:
            if whatOrdered.name == inventory.name:
                inventory.quantity -= whatOrdered.quantity
                try:
                    ourofstockError4(inventory.quantity)
                except orderError as e:
                    return e

    def displayInventory(self):
        for inventory in self._stock:
            print(inventory)

    def checkSpecificInventory(self, name):
        for inventory in self._stock:
            if name == inventory.name:
                print(inventory.name + " within " + str(inventory.quantity) + 'store in inventory' )

    #def addOrder(self,order):
    #    self._orders.append(order)

    def makeOrder(self, mains, extras, status, orderID):

        order = Order(status,orderID)
        for main in mains:
            order.addMain(main)
        for extra in extras:
            order.addExtra(extra)

        self._orders.append(order)
        print(order)
        return order


    def deleteOrder(self,orderID):
        for order in self._orders:
            if order.orderID == orderID:
                self._orders.remove(order)

    def displayOrder(self,orderID):
        for order in self._orders:
            if order.ordersID == orderID:
                print(order)

    def getStockBasePrice(self,name):
        for inventory in self._stock:
            if name == inventory.name:
                return inventory.basePrice

    def updateMealStatus(self,orderID):
        for order in self.orders:
            if order.orderID == orderID:
                order.status = "ready to pick up"

    def checkMealStatus(self,orderID):
        for order in self.orders:
            if order.orderID == orderID:
                return order.status

    def findorder(self, orderID):
        i = None
        for order in self.orders:
            if orderID == order.orderID:
                i = 'find it '
        return i

    def reduce(self):
        for order in self.orders:
            if order.reduce == 'not':
                self.reduceorder(order.orderID)
                self.updateredcue(order)


    def removeorder(self):
        for order in self.orders:
            if order.status == 'ready to pick up':
                self.deleteOrder(order.orderID)


    def updateredcue(self, order):
        order.reduce = 'yes'



    def reduceorder(self, ID):
        i = ID
        for order in self.orders:
            if order.orderID == i:
                for main in order.mainFoods:
                    for ingre in main.ingredient:
                        self.reduceStock(ingre)
                    #for patty in main._patties
                #for extra in order.extraFoods.ingredient:
                #    self.reduceStock(extra)

    def getorder(self,ID):
        for order in self.orders:
            if order.orderID == ID:
                return order

    def checkname(self,name):
        i = False
        for n in self.stock:
            if(n.name == name):
                i = True
        return i

    @property
    def stock(self):
        return self._stock

    @property
    def orders(self):
        return self._orders
