#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:52:03 2024

@author: ihe027
"""




def name_request(**kid):
  print("His first name is " + kid["mname"])

name_request(fname = "Tobias", lname = "Refsnes", mname="Mathias")



def country_function(country = "Norway"):
  print("I am from " + country)

country_function("Sweden")
country_function("India")
country_function()
country_function("Brazil") 


def my_calculations(x):
  return 5 * x

print(my_calculations(3))
print(my_calculations(5))
print(my_calculations(9))

def myfunction():
  pass

myfunction()

def my_recursion(k):
  if(k > 0):
    result = k - 1
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
my_recursion(6)