#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:22:16 2023

Very short introduction to sets and tuples

@author: yin
"""

### SETS

numset = {1, 2, 3, 2}

list_with_duplicates = [1, 1, 2, 4, 7, 8, 8]

uniq_nums = set(list_with_duplicates)

fruitset = {'apple', 'orange', 'banana', 2}

# set operations
# numset = {1,2,3}
# uniq_nums = {1, 2, 4, 7, 8}

union = numset | uniq_nums
intersection = numset & uniq_nums
difference = uniq_nums - numset

### TUPLES
coordinate = (0.1, 5, 5)

print(coordinate.count(5))
print(coordinate.index(5)) 






