#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:25:36 2023

Practice with booleans

@author: yin
"""

# booleans are True / False values 

print(bool(1))
print(bool(0))

all_ok = True

# booleans from strings
astr = 'Hi'
bstr = ''

print(bool(astr))
print(bool(bstr))


# basic if statement
astr = 'Bye'
if astr == 'Hi':
    print('We have been greeted')
elif astr == 'Bye':
    print('Goodbye')
else:
    print('Nobody said hello today')













