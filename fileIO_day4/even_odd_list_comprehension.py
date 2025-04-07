#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:56:32 2023

List comprehension for even and odd

1. takes in list of numbers
2. finds unique values
3. gives back another list with 'even' and 'odd' according to
   your input list
   
   
BONUS: make a dictionary with key as the number 
       and value as 'even' or 'odd'

@author: yin
"""

numlist = [0, 89, 10, 4, 5, 5]
uniqnumlist = list(set(numlist))

even_odd_list = ['even' if num % 2 == 0 else 'odd' for num in uniqnumlist]

# BONUS {key:val for i in range}
even_odd_dict = {uniqnumlist[i] : even_odd_list[i] for i in range(len(uniqnumlist))}

even_odd_dict_w_zip = dict(zip(uniqnumlist, even_odd_list))




