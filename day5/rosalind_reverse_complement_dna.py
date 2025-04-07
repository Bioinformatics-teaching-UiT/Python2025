#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:37:42 2023

Reverse complement of a DNA sequence

@author: yin
"""

ourseq = 'AAAACCCGGT'

def reverse_complement(dnaseq):
    
    complement_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    
    # reverse your dna
    rev_dna = dnaseq[::-1]
    print(rev_dna)
    # complement your dna
    comp_list = []
    for nucl in rev_dna:
        comp_list.append(complement_dict[nucl])
    
    revcomp_dnaseq = ''.join(comp_list)
    
    return revcomp_dnaseq
