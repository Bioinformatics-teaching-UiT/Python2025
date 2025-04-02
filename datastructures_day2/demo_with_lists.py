#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:12:20 2023

Demo with lists

@author: yin
"""

# making a list
mylist = ['apple', 'orange', 31, True]

# get the orange from the list with indexing
print(mylist[1])
print(mylist[-1])
print(mylist[1:])

print(mylist[::-1])


# add kiwi to mylist with append
mylist.append('kiwi')
print(mylist)

# + operator 
mylist = mylist + ['kiwi']
print(mylist)

# count occurrences of kiwi in our list
howmanykiwi = mylist.count('kiwi')
print(howmanykiwi)










