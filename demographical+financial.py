# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:21:14 2022

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
      
      
class employee (person):  
    def __init__(self, name, age, location,salary):
        self.salary=salary
        
        person.__init__(self, name, age, location)        
        
    def details(self):
        print("hi,my name is",self.name)
        print("And my age is",self.age)
        print("I'm staying in",self.location)
        print("my salary is",self.salary)
        
p1 = employee ("Ajay", 36,"HYD",10000)
# p1.display()
p1.details()

