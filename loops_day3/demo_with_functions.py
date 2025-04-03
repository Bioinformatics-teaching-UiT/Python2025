#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:56:44 2023

Demo with functions

@author: yin
"""

# define a greeter function

def greeter(message):
    print(message)

greeter('Today is Wednesday')
greeter(12345)
greeter(True)
greeter(None)

# define a function that returns a value

def square(num):
    squared = num**2
    return squared

two_squared = square(2)
print(two_squared)

# arbitrary number of arguments

def greeter_v_2(*names):
    for name in names:
        print(f'Hello {name}.')
        
# defining a default value

def greeter_v_3(name, msg = 'Hello'):
    print(msg, name)
        






