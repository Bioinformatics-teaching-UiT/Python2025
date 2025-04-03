#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:28:45 2023

Invert string exercise:
    
Function takes a string and returns all the cases swapped

@author: yin
"""

# str.swapcase()

def string_inverter(string):
    """
    Takes in string and swaps the case.
    Non-alphabetical characters stay the same.

    Parameters
    ----------
    string : str

    Returns
    -------
    inv_str : str
        string with swapped case

    """
    inv_str = ''
    
    for char in string:
        if not char.isalpha():
            inv_str += char
        elif char.islower():
            inv_str += char.upper()
        else:
            inv_str += char.lower()
    return inv_str

