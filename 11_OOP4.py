##Giving the datatype to be received
class Item:
  def __init__(self, name : str, price: float, quantity = 0): ##called automatically when the instance is created
    ## Run validations to received arguments
    assert price >= 0, f"Price {price} is not greater than or equal zero!"
    assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

    ## Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity

  ##methods are functions insode the class
  def calculate_total_price(self):
    return self.price * self.quantity

item1 = Item("Phone", 500000, 5)
print(item1.calculate_total_price())

item2 = Item("Laptop", 15000000, 3)
print(item2.calculate_total_price())