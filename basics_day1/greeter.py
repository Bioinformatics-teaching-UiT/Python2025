"""
greeter.py

Friendly greeting program:

    This program says hello, asks for your name,
    and prints a greeting with the given name

Use the input function, print function, and f-strings.

BONUS: Give the program your full name and print out your first
and last name separately! 
"""

# ask the user for their name
fullname = input('Please type in your full name, separated by a space: ')

namelist = fullname.split()
print(namelist[0])
print(namelist[1])

# put the name in an f-string
message = f'Hello {namelist[0]}, your last name is {namelist[1]}.'

# print out the greeting message
print(message)
