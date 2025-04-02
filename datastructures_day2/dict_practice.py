"""
dict_practice.py

In this exercise you will practice with dictionary methods

Follow the instructions below
"""

# make a dictionary that called number_names that stores as 
# keys the numbers from 1 to 5 in words, and as values the integers themselves
# so, an example of an entry would be where the key is 'two' and the value is 2

number_names = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# get the value corresponding to the key 'four'

print(number_names['four'])

print(number_names.get('four'))

# get a list of all the keys in this dictionary

keylist = list(number_names.keys())
print(keylist)

# get a list of all the values in this dictionary

print(list(number_names.values()))

# delete the last entry of the number_names

number_names.popitem()
print(number_names)

# remove the 'two' entry

number_names.pop('two')
print(number_names)

# count the number of entries and print this out
# again, do this programmatically! we are not testing if you can count ;)
print(f'Your dictionary is {len(number_names)} entries long.')



# delete all the values from the dictionary, what do you get?
number_names.clear()
print(number_names)