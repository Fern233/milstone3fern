from inventory import Inventory
from system import System
from food import Burger
from food import Extra
from food import Wrap
from ingredient import Ingredient
from order import Order

print('setting up system')
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
order1 = sys.makeOrder([burger], [side], 'Preparing', 1)

burger32 = Burger()
whiteBun32 = Ingredient('White Bun', sys.getStockBasePrice('White Bun'), 4)
beefPatty32 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 2)
lettuce32 = Ingredient("Lettuce", sys.getStockBasePrice("Lettuce"), 4)
burger32.addBuns(whiteBun32)
burger32.addPatties(beefPatty32)
burger32.addIngredient(lettuce32)

burger_price = burger32.calculatePrice()
assert burger_price == 32

# make a wrap
wrap32 = Wrap()
wholemealWrap32 = Ingredient('Wholemeal Wrap', sys.getStockBasePrice('Wholemeal Wrap'), 1)
chickenPatty32 = Ingredient("Chicken Patty", sys.getStockBasePrice('Chicken Patty'), 2)
beefPatty3 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 1)
wrap32.addIngredient(wholemealWrap32)
wrap32.addPatties(chickenPatty32)
wrap32.addPatties(beefPatty3)
wrap_price = wrap32.calculatePrice()
drink32 = Extra()
coke32 = Ingredient("Small Coca Cola", sys.getStockBasePrice("Can Coca Cola"), 2)
drink32.addExtra(coke32)
drink_price = drink32.calculatePrice()
order2 = sys.makeOrder([burger32, wrap32], [drink32], 'Preparing', 2)


wrap32 = Wrap()
wholemealWrap32 = Ingredient('Wholemeal Wrap', sys.getStockBasePrice('Wholemeal Wrap'), 1)
chickenPatty32 = Ingredient("Chicken Patty", sys.getStockBasePrice('Chicken Patty'), 2)
beefPatty3 = Ingredient("Beef Patty", sys.getStockBasePrice('Beef Patty'), 1)
wrap32.addIngredient(wholemealWrap32)
wrap32.addPatties(chickenPatty32)
wrap32.addPatties(beefPatty3)
wrap_price = wrap32.calculatePrice()
drink32 = Extra()
coke32 = Ingredient("Small Coca Cola", sys.getStockBasePrice("Can Coca Cola"), 2)
drink32.addExtra(coke32)
drink_price = drink32.calculatePrice()
order3 = sys.makeOrder([burger32, wrap32], [drink32], 'ready to pick up', 3)