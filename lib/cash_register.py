#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.items = list()
    self.total = 0
    # extra variables created to keep track of purchases & total in one place
    self.cart = list()
    self.subtotal = 0
    
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    if isinstance(discount, int) and discount >= 0:
      self._discount = discount

  def add_item(self, title, price, quantity = 1):
    # following 5 lines to add items to list() of dicts() 
    cart_item = {"prod": title,
            "price": price,
            "quantity": quantity} 
    self.cart.append(cart_item)
    self.total = self.total + (price*quantity)
    # og technique to pass early tests
    for item in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
      return self.total
    else: 
      self.total -= ((self.discount/100) * self.total)
      print(f"After the discount, the total comes to ${round(self.total)}.")

  def void_last_transaction(self): 
    # below lines are removing the last transaction, but totals (self.total and self.subtotal) are incorrect for the test, though correct for the corresponding carts, which appear to have all of the items added from earlier tests, not just the void_last_transaction tests
    if len(self.items) <= 0:
      self.total = 0
      return self.total
    else:
      item_to_void = self.items[-1] 
      self.items = [elem for elem in self.items if elem != item_to_void]
      del self.cart[-1]
      breakpoint()
      self.subtotal = sum([(item["price"]*item["quantity"]) for item in self.cart ])
      self.total = self.subtotal
    return self.total
      
    # below are attempts to solve using only the self.items list() 
    # for thing in self.cart:
    #   self.subtotal += (thing["price"]*thing["quantity"])
# break **** next 2 lines work for list, but don't alter total so don't pass tests
    # item_to_void = self.items[-1] 
    # self.items = [elem for elem in self.items if elem != item_to_void]
    # break
    # self.items.reverse()
    # for index, a in enumerate(self.items):
    #   for b in self.items[index+1]:
    #     if a != b: 
    #       self.items.reverse().pop()
    #     else:
          