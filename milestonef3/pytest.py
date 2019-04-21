from inventory import Inventory
from system import System
from food import Burger
from food import Extra
from food import Wrap
from ingredient import Ingredient
from order import Order
import pytest


print('setting up system')
@pytest.fixture
def sys():
    sys = System()
    muffinBun= Inventory("Muffin Bun", 4, 50)
    whiteBun = Inventory("White Bun", 2, 150)
    glutenfreeBun = Inventory('Gluten Free Bun',3, 3)
    wholemealWrap = Inventory("Wholemeal Wrap", 1, 150)
    glutenfreeWrap = Inventory('Gluten Free Wrap',2,100)
    beefPatty = Inventory("Beef Patty", 10, 100)
    chickPatty = Inventory('Chicken Patty',5,100)
    lettuce = Inventory("Lettuce", 1, 30)
    frenchFriesS = Inventory("Small French Fries", 3, 130)
    frenchFriesL = Inventory("Large French Fries", 3, 130)
    chickenNuggetS = Inventory("Small Chicken Nuggets", 5, 100)
    chickenNuggetL = Inventory("Large Chicken Nuggets", 7, 100)
    fanta = Inventory("Fanta", 3, 100)
    cokeCan = Inventory("Can Coca Cola", 3, 100)
    cokeBottle = Inventory('Bottle Coca Cola',4,100)

    # for test us 2。1
    SweetBun = Inventory('Sweet Bun',2,3)
    BlackBun = Inventory('Black Bun',1,4)

    sys.addStock(muffinBun)
    sys.addStock(whiteBun)
    sys.addStock(wholemealWrap)
    sys.addStock(beefPatty)
    sys.addStock(whiteBun)
    sys.addStock(wholemealWrap)
    sys.addStock(glutenfreeWrap)
    sys.addStock(cokeCan)
    sys.addStock(cokeBottle)
    sys.addStock(wholemealWrap)
    sys.addStock(lettuce)
    sys.addStock(frenchFriesS)
    sys.addStock(frenchFriesL)
    sys.addStock(chickenNuggetS)
    sys.addStock(chickenNuggetL)
    sys.addStock(fanta)
    sys.addStock(chickPatty)
    sys.addStock(glutenfreeBun)


    # for test us 2.1
    sys.addStock(SweetBun)
    sys.addStock(BlackBun)

    return sys
#######################################################
def testMKOrder(sys):
    #order = Order('parparing',1)
    burger = Burger()
    muffinBun1 = Ingredient("Muffin Bun", sys.getStockBasePrice("Muffin Bun"), 2)
    beefPatty1 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 1)
    sys.reduceStock(muffinBun1)
    sys.reduceStock(beefPatty1)
    burger.addBuns(muffinBun1)
    burger.addPatties(beefPatty1)

    side = Extra()
    chickenNuggetL1 = Ingredient('Large Chicken Nuggets',sys.getStockBasePrice("Large Chicken Nuggets"),1)

    side.addExtra(chickenNuggetL1)

    print("======= receipt ========")
    order1 = sys.makeOrder([burger],[side],'parparing',1)
    print('========================')
    #assert error == None
    assert burger.calculatePrice() == 18
    assert side.calculatePrice() == 7
    assert order1.totalPrice() == 25
    #assert len(sys.orders) == 1
    print('test 1 passed')

#######################################################

def test_MKOrder_alt1(sys):
    order = Order('parparing',2)
    wrap = Wrap()
    wholemealWrap1 = Ingredient('Wholemeal Wrap',sys.getStockBasePrice('Wholemeal Wrap'),3)
    beefPatty1 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 1)

    error = wrap.addWrap(wholemealWrap1)
    wrap.addPatties(beefPatty1)
    order.addMain(wrap)
    #assert len(sys.orders) == 1
    print("=======error=======")
    print(error)
    print("====================")
    print('test 2 passed')

#######################################################
def test_MKOrder_alt2(sys):
    order = Order('parparing',3)
    burger1 = Burger()
    whiteBun1 = Ingredient('White Bun',sys.getStockBasePrice('White Bun'),5)
    beefPatty1 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 8)
    lettuce1 = Ingredient("Lettuce", sys.getStockBasePrice('Lettuce'),3)

    error1 = burger1.addBuns(whiteBun1)
    error2 = burger1.addPatties(beefPatty1)
    burger1.addIngredient(lettuce1)

    print("=======error=======")
    print(error1)
    print(error2)
    print('===================')
    print('test 3 passed')

#######################################################
def test_MKOrder_alt3(sys):
    burger1 = Burger()
    whiteBun1 = Ingredient('White Bun', sys.getStockBasePrice('White Bun'), 4)
    beefPatty1 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 2)
    lettuce1 = Ingredient("Lettuce", sys.getStockBasePrice("Lettuce"), 3)

    error1 = burger1.addBuns(whiteBun1)
    error2 = burger1.addPatties(beefPatty1)
    burger1.addIngredient(lettuce1)

    assert error1 == None
    assert error2 == None
    assert burger1.calculatePrice() == 31

    wrap1 = Wrap()
    wholemealWrap1 = Ingredient('Wholemeal Wrap', sys.getStockBasePrice('Wholemeal Wrap'), 1)
    chickenPatty2 = Ingredient("Chicken Patty", sys.getStockBasePrice('Chicken Patty'), 2)

    error3 = wrap1.addWrap(wholemealWrap1)
    error4 = wrap1.addPatties(chickenPatty2)

    assert error3 == None
    assert error4 == None
    assert wrap1.calculatePrice() == 11

    # order.addMain(burger1)
    # order.addMain(wrap1)
    print("======= receipt ========")
    order2 = sys.makeOrder([burger1, wrap1], [], "preparing", 4)
    print('========================')
    assert order2.totalPrice() == 42
    print("test 4 passed")

    #assert len(sys.orders) == 2



def test_MKOrder_alt4(sys):

    drink = Extra()
    fanta1 = Ingredient('Fanta',sys.getStockBasePrice('Fanta'),5)

    drink.addExtra(fanta1)

    assert drink.calculatePrice() == 15

    print("======= receipt ========")
    order4 = sys.makeOrder([],[drink],'preparing',4)
    print('=========================')
    assert order4.totalPrice() == 15
    assert order4.mainFoods == []
    #assert  len(sys.orders) == 3
    print("test 5 passed")


#Test us2_1: On the next page, customer is able to add sides/drink ,
#            which base on how many inventory left.
#            If the inventory shows zero, then it will not selectable in customer page.


def test_us2_1(sys):

    #order21 = Order('preparing', 21)

    burger1 = Burger()
    muffinBun1 = Ingredient("Muffin Bun", sys.getStockBasePrice("Muffin Bun"), 2)
    beefPatty1 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 1)
    burger1.addBuns(muffinBun1)
    burger1.addPatties(beefPatty1)

    burger2 = Burger()
    GBun2 = Ingredient("Gluten Free Bun", sys.getStockBasePrice("Gluten Free Bun"), 4)
    beefPatty2 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 2)
    burger2.addBuns(GBun2)
    burger2.addPatties(beefPatty2)

    print("======= receipt ========")
    order5 = sys.makeOrder([burger1,burger2], [], 'preparing', 21)
    assert order5.totalPrice() == 50
    assert len(order5.mainFoods) == 2
    sys.reduceStock(muffinBun1)
    sys.reduceStock(beefPatty1)
    #sys.checkcheckSpecificInventory(muffinBun1)
    print("======= errors ========")
    error1 = sys.reduceStock(GBun2)
    sys.reduceStock(beefPatty2)

    print(error1)
    print('test us2_1 has finished')
    print('')

def test_us2_1_2(sys):

    burger12 = Burger()
    sweetbun12 = Ingredient("Sweet Bun", sys.getStockBasePrice("Sweet Bun"), 2)
    chickpatty12 = Ingredient("Chicken Patty", sys.getStockBasePrice('Chicken Patty'), 1)
    error12 = burger12.addBuns(sweetbun1)
    error12 = burger12.addPatties(chickpatty1)

    burger12 = Burger()
    sweetbun12 = Ingredient("Sweet Bun", sys.getStockBasePrice("Sweet Bun"), 2)
    chickpatty12 = Ingredient("Chicken Patty", sys.getStockBasePrice('Chicken Patty'), 1)
    error13 = burger12.addBuns(sweetbun12)
    error14 = burger12.addPatties(chickpatty12)

    error1 =  sys.reduceStock()
    assert error13 == None
    assert error12 == None
    assert error1 == 'Sorry it is out stock'
    assert error14 == None

    print('test us2_1_2 has finished')
# can not make order in this case

def test_us2_1_3(sys):

    frenchFriess213 = Ingredient("French Fries", sys.getStockBasePrice("Small French Fries"), 2)
    fanta213 = Ingredient("Fanta", sys.getStockBasePrice("Fanta"), 1)
    chickenNuggets213 = Ingredient("Small Chicken Nuggets", sys.getStockBasePrice("Small Chicken Nuggets"), 1)


    side213 = Extra()
    side213.addExtra(frenchFriess213)
    side213.addExtra(fanta213)
    side213.addExtra(chickenNuggets213)

    assert len(side213.ingredient) == 3
    order213 = sys.makeOrder([], [side213], 'preparing', 213)
    print("test us2_1_3 has finished \n")




#Test us2_2 if the customer would not have any sides, they can skip the page.

def test_us2_2(sys):


    burger3 = Burger()
    whiteBun1 = Ingredient("White Bun", sys.getStockBasePrice("White Bun"), 2)
    beefPatty3 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 1)
    sys.reduceStock(whiteBun1)
    sys.reduceStock(beefPatty3)

    burger3.addBuns(whiteBun1)
    burger3.addPatties(beefPatty3)
    print("========= receipt ===========")
    sys.makeOrder([burger3], [], 'preparing', 2)
    print('==============================')
    #assert order22.extraFoods == None

    print('test us2_2 has finished')


#def test_us2_2_2(sys):


#Test 3: Customer can order different size of their drink/sides.
#        2 different sizes are available for drinks(375ml and 600ml) and
#        3 sizes are available for sides(small, medium, large).
#        Size selection is followed by the item selection.

def test_us2_3(sys):

    frenchFriess1 = Ingredient("French Fries", sys.getStockBasePrice("Small French Fries"), 2)
    frenchFriesl1 = Ingredient("French Fries", sys.getStockBasePrice("Large French Fries"), 2)

    cokel = Ingredient("Coca Cola", sys.getStockBasePrice("Bottle Coca Cola"), 2)
    cokes = Ingredient("Coca Cola", sys.getStockBasePrice("Can Coca Cola"), 3)

    side23 = Extra()
    side23.addExtra(frenchFriess1)
    side23.addExtra(frenchFriesl1)
    side23.addExtra(cokel)
    side23.addExtra(cokes)
    assert len(side23.ingredient) == 4
    print("========= receipt ===========")
    order23 = sys.makeOrder([], [side23], 'preparing', 23)
    print("=============================")
    print('')
    print("test us2_3 finishes \n")

def test_us3_245(sys):

    # make a burger
    burger32 = Burger()
    whiteBun32 = Ingredient('White Bun', sys.getStockBasePrice('White Bun'), 4)
    beefPatty32 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 2)
    lettuce32 = Ingredient("Lettuce", sys.getStockBasePrice("Lettuce"), 4)
    burger32.addBuns(whiteBun32)
    burger32.addPatties(beefPatty32)
    burger32.addIngredient(lettuce32)

    burger_price = burger32.calculatePrice()
    assert burger_price == 32

    #make a wrap
    wrap32 = Wrap()
    wholemealWrap32 = Ingredient('Wholemeal Wrap', sys.getStockBasePrice('Wholemeal Wrap'), 1)
    chickenPatty32 = Ingredient("Chicken Patty", sys.getStockBasePrice('Chicken Patty'), 2)
    beefPatty3 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 1)
    wrap32.addIngredient(wholemealWrap32)
    wrap32.addPatties(chickenPatty32)
    wrap32.addPatties(beefPatty3)

    wrap_price = wrap32.calculatePrice()
    assert wrap_price == 21

    drink32 = Extra()
    coke32 = Ingredient("Small Coca Cola", sys.getStockBasePrice("Can Coca Cola"), 2)
    drink32.addExtra(coke32)
    assert coke32.quantity == 2

    drink_price = drink32.calculatePrice()
    assert drink_price == 6
    print("========= receipt ===========")
    order = sys.makeOrder([burger32,wrap32], [drink32],'Preparing', 4)
    print("=============================")
    assert order.totalPrice() == 59
    #assert len([]) == 2
    #assert len(order32.extraFoods) == 1
    #totalPrice = order32.totalPrice()
    #assert totalPrice == 59

    print("test us3_245 have finished\n")

# Test  us4_1: Once, a customer has completed their selection (main, side and drink),
#              they can checkout to complete their order, then the system will automatically
#              print a receipt (meal confirmation) for them to confirmation what they order.
#       us4_2 the receipt will include what the customer have ordered and the total price of this meal.

def test_us4_1_2(sys):

    # order some drinks
    drink412 = Extra()
    fanta1 = Ingredient('Fanta', sys.getStockBasePrice('Fanta'), 5)
    drink412.addExtra(fanta1)

    # order a burger
    burger412 = Burger()
    whiteBun412 = Ingredient('White Bun', sys.getStockBasePrice('White Bun'), 4)
    beefPatty412 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 2)
    lettuce412 = Ingredient("Lettuce", sys.getStockBasePrice("Lettuce"), 3)
    burger412.addIngredient(whiteBun412)
    burger412.addIngredient(lettuce412)
    burger412.addPatties(beefPatty412)

    # order a side
    side412 = Extra()
    frenchFries412 = Ingredient("friess",sys.getStockBasePrice('Small French Fries'),2)
    side412.addExtra(frenchFries412)
    print("========= receipt ===========")
    o = sys.makeOrder([burger412],[drink412,side412],'preparing',6)
    assert o.totalPrice() == 52
    print("test us4_1_2 has finished \n")

##  ready to pick up and preparing
#Test us5_1:
#     us5_2: At any point in time, the customer will be able to check if their order
#            is ready to be collected using their order-id.
#            The customer can check the status of their order at any point to see if their order is completed.

#Test  us8_1: Display the current order information on the staff page.###?????????????????????
#      us8_2: Staff would be able to update the status of meal. ####### same as us5?????
#      us8_3:
#      us8_4: Once customer collected their orders, staff could be able to
#             remove those orders from staff interface by clicking “finish” button.????????????
              # i change it into deleteorder  and i wanna merge it with us 5

def test_us5withus8(sys):

    current_status = sys.checkMealStatus(6)
    assert current_status == 'preparing'
    sys.updateMealStatus(6)
    assert (sys.checkMealStatus(6)) == 'ready to pick up'
    sys.deleteOrder(6)
    assert sys.findorder(6) == None
    print("test us5 and us 8 have finished\n")



def test_us_6(sys):

    #frenchFriesS = Inventory("Small French Fries", 3, 130)
    assert sys.frenchFriesS.quantity == 130
    side6 = Extra()
    frenchFries6 = Ingredient("Small French Fries", sys.getStockBasePrice("Small French Fries"), 2)
    assert frenchFries6.quantity == 2
    side6.addExtra(frenchFries6)
    sys.reduceStock(frenchFries6)
    assert sys.frenchFriesS.quantity == 128
    sys.refillStock("Small French Fries", 4)
    assert sys.frenchFriesS.quantity == 132

    print("test us6 has finished\n")


def test_us_6(sys):

    #frenchFriesS = Inventory("Small French Fries", 3, 130)
    assert sys.frenchFriesS.quantity == 130
    side6 = Extra()
    frenchFries6 = Ingredient("Small French Fries", sys.getStockBasePrice("Small French Fries"), 2)
    assert frenchFries6.quantity == 2
    side6.addExtra(frenchFries6)
    sys.reduceStock(frenchFries6)
    assert sys.frenchFriesS.quantity == 128
    sys.refillStock("Small French Fries", 4)
    assert sys.frenchFriesS.quantity == 132

    print("test us6 has finished\n")

#########
#Test - How does the inventory list look likes.
#Test – If a particular item/ingredient is below than standard amount,
# As a customer places an order will result in the inventory levels being decremented accordingly.
# Test: Bottled drinks are stocked in either cans (375 ml) or bottles (600 ml)
# and drinks such as cokes will be served in varying sizes
# (e.g., a small = 250 ml, a medium = 450 ml etc).
#Test: Sides such as fries will need to be stocked by weight (in gms).
# The size include small(75g), a medium(125g), so the inventory level will be decrement by weight.

def test_us_7(sys):

    # add some different sizes of sides and drinks in to inventory
    frenchFriesS7 = Ingredient("Small French Fries", sys.getStockBasePrice("Small French Fries"),5)
    frenchFriesL7 = Ingredient("Large French Fries", sys.getStockBasePrice("Large French Fries"),5)
    frenchFriesM7= Ingredient("Medium French Fries", sys.getStockBasePrice("Medium French Fries"),5)
    cokeL7 = Ingredient("Large Coca Cola", sys.getStockBasePrice("Large Coca Cola"),2)
    cokeS7 = Ingredient("Small Coca Cola", sys.getStockBasePrice("Small Coca Cola"),3)

    side7 = Extra()
    drink7 = Extra()

    side7.addExtra(frenchFriesS7)
    side7.addExtra(frenchFriesL7)
    side7.addExtra(frenchFriesM7)

    drink7.addExtra(cokeL7)
    drink7.addExtra(cokeS7)

    print(side7)
    print(drink7)
    print("test us7 has finished\n")




# update meal status
def test_UpdateStatus(sys):
    current_status = sys.checkMealStatus(21)
    assert current_status == 'preparing'
    sys.updateMealStatus(21)
    assert (sys.checkMealStatus(21)) == 'ready to pick up'
    sys.deleteOrder(21)

    current_status = sys.checkMealStatus(2)
    assert current_status == 'preparing'
    sys.updateMealStatus(2)
    assert (sys.checkMealStatus(2)) == 'ready to pick up'
    sys.deleteOrder(2)

    print("test updating status has finished\n")


# delete order
def test_DeletOrder(sys):
    # delete the previous order 6
    sys.deleteOrder(6)
    i = sys.findorder(6)
    assert i == None

    # delete the previous order 21
    sys.deleteOrder(21)
    a = sys.findorder(21)
    assert a == None

    print("test delecting order 1 has finished\n")

def test_DeletOrder_1(sys):

    sys.deleteOrder(4)
    i = sys.findorder(4)
    assert i == None

    # delete the previous order 21
    sys.deleteOrder(2)
    a = sys.findorder(2)
    assert a == None

    print("test delecting order 2 has finished\n")