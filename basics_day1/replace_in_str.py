"""
replace_in_str.py

Replace Within a String

This script takes in a string with words separated by commas,
and replaces the commas with spaces.
Then it prints out the resulting string.
"""

# replace(old,new,count), if count isn't given, default to all

somestr = 'words   ,separated,with, comma,'

print(somestr.count(',')) # count instances of commas in somestr
commareplaced = somestr.replace(',', ' ') # replace spaces with commas
print(commareplaced)
