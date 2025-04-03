#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:25:34 2023

Calculate mean from list of numbers

@author: yin
"""

def get_mean(numlist):
    """
    This function calculates the mean value.

    Parameters
    ----------
    numlist : list
        list of numbers

    Returns
    -------
    mean_val : int, float
        value corresponding to the mean
    """
    sum_val = 0
    for number in numlist:
        sum_val += number
    mean_val = sum_val / len(numlist)
    return mean_val

def get_mean_short(numlist):
    mean_val = sum(numlist) / len(numlist)
    return mean_val

