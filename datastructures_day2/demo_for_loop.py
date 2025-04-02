#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:46:40 2023

Demo with for loops

@author: yin
"""

# basic for loop to loop over the numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#for i in numbers:
#    print(i)
    
# range function as iterating range
for i in range(8):
    print(i)
print('Done\n')

# for loop behaviour over strings
astr = 'abcdefg'

for i in astr:
    print(i)
print('\n')
    
# break statement
for i in numbers:
    if i == 5:
        break
    print(i)
print('\n')

# continue statement
for i in numbers:
    if i == 5:
        continue
    print(i)



