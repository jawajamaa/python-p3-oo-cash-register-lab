#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.items = list()
    # self.items_total = dict() can't use; needs to be unique key...
    self.total = 0
    
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    if isinstance(discount, int) and discount >= 0:
      self._discount = discount

  def add_item(self, title, price, quantity = 1):
    self.total = self.total + (price*quantity)
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
    item_to_void = self.items[-1] 
    breakpoint()
    self.items = [elem for elem in self.items if elem != item_to_void]
    breakpoint()
    # self.items.reverse()
    # for index, a in enumerate(self.items):
    #   for b in self.items[index+1]:
    #     if a != b: 
    #       self.items.reverse().pop()
    #     else:
          