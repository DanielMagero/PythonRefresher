class Item:
  def __init__(self, name, price, quantity = 0): ##called automatically when the instance is created
    print(f"An instance created: {name}")
    self.name = name
    self.price = price
    self.quantity = quantity

  ##methods are functions insode the class
  def calculate_total_price(self, x, y):
    return x * y

item1 = Item("Phone", 500000, 5)
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("Laptop", 15000000, 3)
print(item2.calculate_total_price(item2.price, item2.quantity))

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
