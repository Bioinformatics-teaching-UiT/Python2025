"""
guess_the_number.py

Let's play a game where you ask the user to input a number,
see if it matches your own number, 
and you tell the user if the number is correct or not.

If it is correct, end the game. If not, continue.

"""

# setting our numbers

guess_num = input('Please give a whole number:\n')
actual_num = 20

   
# while loop to enter the game
while True:
    if guess_num != actual_num:
        print('Wrong number.')
        guess_num = int(input('Please give another number:\n'))
    else:
        break
    
# another way to write while loop
# while guess_num != actual_num:
#     guess_num = int(input('Please give another number:\n'))
# print('Congrats.')
    
