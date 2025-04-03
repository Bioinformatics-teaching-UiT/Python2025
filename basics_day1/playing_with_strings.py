#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Playing with Strings

Script with string operations

@author: yin
"""

# practice with input function

#hello_str = 'Hello '
#username = input('Please type a name: ')
#print('Hello', username)

# variables can change type, check with type()
my_variable = 'monday'
print(type(my_variable))
my_variable = 100
print(type(my_variable))
print(my_variable)

# switch from an int to a string
hundred = 100
hundred_str = str(hundred)
print(hundred_str)

# string slicing
message = 'HelloWorld'

print(message[:5]) # gives 'Hello'
print(message[5:]) # gives 'World'

print(message[0:5:2]) # gives 'Hlo'
print(message[-1]) # gives 'd'

print(message[::-1]) # gives reverse
print(message)

# capitalise method
newstr = 'alllowercase'
print(newstr.capitalize())

# strip method
strwithwhitespace = "       sometext       "
print(strwithwhitespace.strip())

# replace method
numbers = 'one, two, three, four'
numbers_hyphen = numbers.replace(' ', '-')
print(numbers)
print(numbers_hyphen)

# lower method
print('ABC'.lower())

# split method
print(numbers.split(', '))

# f-str
name = 'jane'
message = f'{name} is a student'
print(message)

# add two strings
print('firstpart' + 'secondpart')

# duplicate/multiply strings
print('onetime'*10)















