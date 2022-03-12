# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:33:10 2022

@author: sys
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:28:45 2022

@author: sys
"""

class income ():
  def __init__(self, salary):
    self.salary = salary
    
  def display(self): 
      print(self.salary)
    
  def details(self):

      print("my salary is",self.salary)
     
p = income(10000)
p.details()

