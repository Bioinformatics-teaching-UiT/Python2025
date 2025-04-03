"""
FizzBuzz exercise

Write a script that goes through the numbers 1 to 100.

If the number is divisible by 3 and 5, output 'FizzBuzz'.

If the number is divisible by 3 (but not 5), output 'Fizz'.

If the number is divisible by 5 (but not 3), output 'Buzz'.

Otherwise, just print out the number.
"""

# Sounds like a for-loop with if-statements
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    elif n % 5 == 0 and n % 3 != 0:
        print("Buzz")
    else:
        print(n)

# Works fine
