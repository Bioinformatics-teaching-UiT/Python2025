#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:57:01 2023

Rosalind Exercise number 1: count nucleotides

@author: yin
"""

ourseq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# loop over the sequence

def nucl_counter_seqloop(sequence):
    """Counts nucleotides in sequence, saves to dict with counts"""
    nucl_counts = {'A':0, 'T':0, 'C':0, 'G':0}
    
    for nucl in sequence:
        nucl_counts[nucl] = nucl_counts[nucl] + 1
        
    return nucl_counts

# loop over the four nucleotides, use seq.count()

def nucl_counter_loop2(sequence):
    """Counts nucleotides in seq, loops over ATCG, saves to dict"""
    nucl_counts = {'A':0, 'T':0, 'C':0, 'G':0}
    
    for nucl in ['A','C','T','G']:
        nucl_counts[nucl] = sequence.count(nucl)
        
    return nucl_counts
        
        
countsdict = nucl_counter_loop2(ourseq)


# print it out in order A C G T

#print(countsdict['A'], countsdict['C'], countsdict['G'], countsdict['T'])
        
#print(ourseq.count('A'), ourseq.count('C'), ourseq.count('G'), ourseq.count('T'))

# BONUS one line
# list comprehension

counts = ' '.join([str(ourseq.count(base)) for base in 'ATCG'])
print(counts) 
    
    
    
    
    

