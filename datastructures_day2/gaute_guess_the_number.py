# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:04:03 2023

@author: Gaute
"""

"""
guess_the_number.py

Let's play a game where you ask the user to input a number,
see if it matches your own number, and you tell the user if the number is correct or not.

If it is correct, end the game. If not, continue.

"""

# Assign a number that is the correct guess
correct_guess = 42
the_guess = ''
yes_str = 'yesYesYES'
no_str = 'noNoNO'
the_magic_word = 'pleasePleaseSesamesesame'
counter = 0

# Ask for input
print('Welcome to "Guess the Number"!')
while the_guess != correct_guess:
    print('Which number am I thinking of?')
    the_guess = int(input())
    print(f'You guessed {the_guess}! \n')
    if the_guess == correct_guess:
        print('Your guess was correct, congratulations!')
        break
    elif counter > 10:
        print('Wow, you are really bad at this! Sorry, I do not want to play with you anymore.')
        break
    else: 
        counter += 1
        print('Sorry, that is incorrect. Would you like to try again?')
        answer = input()
        if answer in no_str:
            print('Ok, thanks for playing!')
            break
        tip_answer = input('Do you want a tip? \n')
        if tip_answer in yes_str:
            magic_word = input('What is the magic word? \n')
            if magic_word in the_magic_word:
                if the_guess > correct_guess:
                    print('The number I am thinking is smaller than your guess.')
                elif the_guess < correct_guess:
                    print('The number I am thinking of is bigger than your guess.')
            elif magic_word == 'cheatcode':
                print(f'You used a cheat code! The number I am thinking of is {correct_guess}.')
            else:
                print('That is not the magic word. You do not get a tip, sorry!')
                
                
