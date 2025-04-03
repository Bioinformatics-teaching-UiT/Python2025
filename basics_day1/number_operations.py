#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Number operations

This script illustrates the most common number operations
+ , - , * , / , // , % , **

@author: yin
"""
# calculations with integers only produce integers
print(1+1)
print(5-2)
print(5*2)

# combining integers and floats produces floats
print(1.0+1)
print(5-2.0)
print(5.0*2)

# division always produces floats
print(6/2)
print(4.0/3)


# integral division gives you the integer rounded down
print(4//3)
print(-3//2) # weird integral division rounds down

# modular operator gives you a remainder
print(7%3)

# be careful with very precise numbers
print(3*0.1) # numbers are approximations
