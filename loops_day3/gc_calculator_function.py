#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:34:37 2023

GC calculator function

@author: yin
"""

def gc_calculator(seq):
    """
    This function calculates the GC content
    of a sequence, and gives it as a percentage.
    
    Parameters
    ----------
    seq: str
        sequence of DNA

    Returns
    -------
    gc_percentage: float
        number corresponding to % G or C in seq
    """
    gc_count = seq.count('G') + seq.count('C')
    gc_percentage = 100 * (gc_count/len(seq))
    return gc_percentage
    
