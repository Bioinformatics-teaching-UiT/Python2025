#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Apr 18 13:48:29 2023

guess_the_number.py

Let's play a game where you ask the user to input a number,

see if it matches your own number, and you tell the user if the number is correct or not.

If it is correct, end the game. If not, continue.

@author: mga106

"""

#%%

number = 34 
guess = input('Let us play a game: can you guess which number I am thinking of?\n')
guess = int(guess)
i = 0

#%%

while True:
    guess != number
    print('Nope. That is wrong.')
    guess = int(input('Please guess again.\n'))  
    i = i+1   
    if guess == number:
        print('Well done! That is correct!')
        break 
    if i % 5 == 0:
        print('Nope. That is wrong.')
        answer = input('Do you want to give up?.\n')
        if answer == 'yes':
            print('Looser!')
            break