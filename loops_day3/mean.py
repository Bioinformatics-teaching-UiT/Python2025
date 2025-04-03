#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:04:26 2024

@author: ihe027
"""

numlist=[]

for i in range(1,10):
    numlist.append(i) 
    
sum_val = 0
for number in numlist:
    sum_val = sum_val + number**2
    
print(sum_val)

mean_val = sum_val / len(numlist)
print(mean_val)

factorial_val=1
for number in numlist:
    factorial_val *= number
    
    
print(factorial_val)