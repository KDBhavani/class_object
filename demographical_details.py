# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:37:27 2022

@author: sys
"""


class person ():
    
  def __init__(self, name, age, location):
    self.name = name
    self.age = age
    self.location = location
    
  def display(self):
       print(self.name)
       print(self.age)
       print(self.location)
               
      
  def details(self):
      
      print("hi,my name is",self.name)
      print("And my age is",self.age)
      print("I'm staying in",self.location)
      

        
p1 = person ("Ajay", 36,"HYD")
# p1.display()
p1.details()

