#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:45:39 2023

Mean and file reading exercise

Write 3 functions

The first two functions open and close a file and read the 
contents into a list of numbers

The third function calculates the mean of the list of numbers

@author: yin
"""

# define function one with separate open and close 
def num_list_from_file(filename):
    """
    Function reads in a file with numbers.
    Returns a list of the numbers.
    Calls open and close separately

    Parameters
    ----------
    filename : str

    Returns
    -------
    numlist : list
        list of numbers from within the file
    """
    numlist = []
    infile = open(filename, 'r')
    
    for line in infile:
        numlist.append(float(line.strip()))
        
    infile.close()
        
    return numlist

def num_list_from_file_listcomp(filename):
    infile = open(filename, 'r')
    numlist = [float(line.strip()) for line in infile]
    infile.close()
    return numlist





# define function including with statement to open and close
def num_list_from_file_v2(filename):
    """
    Function reads in a file with numbers.
    Returns a list of the numbers.
    Uses the with statement.

    Parameters
    ----------
    filename : str

    Returns
    -------
    numlist : list
        list of numbers from within the file
    """
    with open(filename, 'r') as infile:
        numlist = [float(line.strip()) for line in infile]
    return numlist


# mean function on a list of numbers
def calculate_mean(numlist):
    return sum(numlist)/len(numlist)


# calculate the mean from your file
ourfile = 'numbers.txt'
num_list1 = num_list_from_file(ourfile)
mean_val1 = calculate_mean(num_list1) 

mean_val2 = calculate_mean(num_list_from_file_v2(ourfile))
    
    
    
    
