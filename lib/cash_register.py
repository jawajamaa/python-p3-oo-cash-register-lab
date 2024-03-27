#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.items = list()
    self.total = 0
    
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    if isinstance(discount, int) and discount >= 0:
      self._discount = discount
    # if isinstance(total, int) and total >= 0:
    #   self._total = total

  def add_item(self, title, price, quantity = 1):
    self.total = self.total + (price*quantity)


    # if self.discount == 0:
    #   self.total = self.total + (price*quantity)
    # else:
    #   self.total = (self.total + (price*quantity)) - ((self.discount/100) * self.total)
  

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
      return self.total
    else: 
      self.total -= ((self.discount/100) * self.total)
      print(f"After the discount, the total comes to ${round(self.total)}.")
