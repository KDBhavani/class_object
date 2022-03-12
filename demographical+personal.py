# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 20:04:08 2022

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
      
      
class interests (person):  
    def __init__(self, name, age, location,interest):
        self.interest=interest
        
        person.__init__(self, name, age, location)        
        
    def details(self):
        print("hi,my name is",self.name)
        print("And my age is",self.age)
        print("I'm staying in",self.location)
        print("i'm interested on",self.interest)
        
p1 = interests ("Ajay", 36,"HYD","coin_collection")
# p1.display()
p1.details()



# class person:
# 		

# 	def __init__(self, salary, interest):
# 	
# 		self.salary = salary
# 		self.interest = interest	
# 	
# anusha = person("10000", "dancing")
# akhil = person("20000", "riding")

# print('anusha details:')
# # print('my name is anusha')
# print('salary: ', anusha.salary)
# print('interest: ', anusha.interest)

# print('\nakhil details:')
# # print('my name is akhil')
# print('salary: ', akhil.salary)
# print('interest: ', akhil.interest)

