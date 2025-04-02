"""
test_number_odd_even.py

This script takes in an integer, and tests if it is even or odd.
It then prints out a message to the user with the result.

Use input() function
if/else statement
f-string
BONUS: write the if-statement in one line
"""

# take a number from the user
number = int(input('Please give a whole number:\n'))

print(type(number))

# check this number in an if/else statement
# print out meaningful message

if number % 2 == 0:
    print(f'Your number: {number} is even!')
else:
    print(f'Your number: {number} is odd!')
    

    











