# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:37:18 2022

@author: sys
"""


class interests ():
  def __init__(self, interest):
    self.interest = interest
    
  def display(self):
      print(self.interest)
    
  def details(self):

      print("i'm interested on",self.interest)
     
p = interests("coin_collection")
p.details()