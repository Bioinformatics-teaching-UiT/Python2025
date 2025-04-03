#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:13:32 2023

Demo with file IO (input/output)

@author: yin
"""
# set the file name
numbers_file = 'numbers.txt'

# open the file
infile = open(numbers_file, 'r')

# print out the lines in the file
for line in infile:
    print(line.strip())
    
# close the file
infile.close()

# with statement, automatically closes infile once out of with
# statement
with open(numbers_file, 'r') as infile:
    for line in infile:
        print(line.strip())
        
# readlines() method
with open(numbers_file, 'r') as infile:
    lines = infile.readlines()
    

# write something into a file
outfile = 'new_numbers.txt'

numbers_list = [1,2,3,4,5]

with open(outfile, 'w') as f:
    for number in numbers_list:
        f.write(f'{number}\n')











    
