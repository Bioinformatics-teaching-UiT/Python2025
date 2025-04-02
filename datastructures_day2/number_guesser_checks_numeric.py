#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:26:08 2023

Guess the number, checks if number is numeric

@author: yin
"""

# initialise variables
true_number = 19
guess = input('Please give a whole number: ')

# enter our while loop
while True:
    if guess.isnumeric():
        guess = int(guess)
        if guess == true_number:
            print(f'Congrats! You have guessed correctly: {guess}')
            print('Game over!')
            break
        else:
            guess = input(f'{guess} is wrong. Enter a new number: ')
    else:
        guess = input('You have entered an invalid number. Enter a new number: ')
            