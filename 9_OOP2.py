class Item:
  def __init__(self): ##called automatically when the instance is created
    print("I am created!")

  ##methods are functions insode the class
  def calculate_total_price(self, x, y):
    return x * y

item1 = Item()
item1.name  = "Phone"
item1.price = 500000
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name  = "Laptop"
item2.price = 1500000
item2.quantity = 2
print(item2.calculate_total_price(item2.price, item2.quantity))
 