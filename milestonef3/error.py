
class orderError(Exception):
    pass

def makeOrderError1(buns):
    if buns.quantity > 4:
        raise orderError('Sorry, you cannot order more than 4 buns')

def makeOrderError2(wraps):
    if wraps.quantity > 2:
        raise  orderError('Sorry, this is a wrap')

def makeOrderError3(patties):
    if patties.quantity > 4:
        raise  orderError('Sorry, you cannot order more than 4 patties')

def ourofstockError4(inventorynum):
    if inventorynum < 0:
        raise  orderError('Sorry it is out stock')