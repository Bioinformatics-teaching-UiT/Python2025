#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:23:59 2023

@author: yin
"""

mydna = 'GATGGAACTTGACTACGTAAATT'

myrna = mydna.replace('T', 'U')

def dna_to_rna_long(sequence):
    """ """
    rnalist = []
    for nucl in sequence:
        if nucl == 'T':
            rnalist.append('U')
        else:
            rnalist.append(nucl)
    rnaseq = ''.join(rnalist)
    return rnaseq


def dna_to_rna_short(sequence):
    
    rnalist = ['U' if nucl == 'T' else nucl for nucl in sequence]
    rnaseq = ''.join(rnalist)
    
    return rnaseq



