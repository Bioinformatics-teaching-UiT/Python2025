#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:26:01 2023

Demo with dictionaries

@author: yin
"""

# make a basic dictionary

number_dict = {'zero': 0, 'one': 1, 'two': 2}
print(f'Our dictionary has {len(number_dict)} entries.')


# access entries
print(number_dict['zero'])

# get only the keys from the dictionary
keys = number_dict.keys()
print(keys)
print(type(keys))
print(list(keys))

# get only the values from the dictionary
values = number_dict.values()
print(values)






