##Giving the datatype to be received
class Item:
  ##class atttribute
  pay_rate  = 0.8 ##pay after 20% discount

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
  
  def apply_discount(self):
    self.price  = self.price * self.pay_rate ## self instead of Item to allow instance level assignment

item1 = Item("Phone", 500000, 5)
print(item1.calculate_total_price())

item2 = Item("Laptop", 15000000, 3)
print(item2.calculate_total_price())


print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

#print(Item.__dict__) ## all attributes at class level
#print(item1.__dict__) ## all attributes at instance level

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)