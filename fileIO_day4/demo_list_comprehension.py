#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:40:56 2023

List comprehension

@author: yin
"""

# traditional way to make a list with numbers
numbers = []
stop = 5
for i in range(1, stop+1):
    numbers.append(i)

# list comprehension

numbers_2 = [i+1 for i in range(1, 6)]