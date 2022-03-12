# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:28:45 2022

@author: sys
"""

class income ():
    
  def __init__(self,salary,):
      
    self.salary = salary
    
    
  def display(self):
      
     print(self.salary)
     
    
  def details(self):
      
      print("my salary is",self.salary)
     
      
class interests (income):
    
  def __init__(self,salary,interest):
    self.interest = interest
    
    income.__init__(self, salary)
    
  def details(self):  
     print("my salary is",self.salary)
     print("I'm interested on",self.interest)
     
     
p1 = interests(10000,"coin_collection")
p1.details()
# p1.display()