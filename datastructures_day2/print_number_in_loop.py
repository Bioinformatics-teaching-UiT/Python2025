"""
print_number_in_loop.py

Take in a user given positive integer, and 
print out each number from 0 to your number 
in a for loop

BONUS: skip all odd numbers
       exit if number is higher than or equal to 25
"""

# take in user input number
# convert string input to int

upperbound = int(input('Please give a positive number:\n'))

# loop over over the range from 0 to your number
for i in range(upperbound):
    print(i+1)
    
print('\n')  

for i in range(1,upperbound+1):
    print(i)   


print('\n') 

# skip all odd numbers
for i in range(upperbound):
    if i % 2 != 0:
        continue
    print(i)
    
# clearer way
for i in range(upperbound):
    if i % 2 == 0:
        print(i)
    if i >= 25:
        break
    
    
    
    
    
    
    
    
    