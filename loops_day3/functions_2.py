
# 1. Mean the bean
def mean(numbers: list) -> float: return sum(numbers) / len(numbers)
# Could have checked if the elements is numbers, but not specified in the task.

numbers = [1, 2, 3, 0, -10, 14, 3]
print(mean(numbers)) # Sweet

# 2. String case reverser
def reverser(string: str) -> str: return string[::-1]

string = "dsjbfb f sdojahb AHJEDB"

print(reverser(string)) # Simple as that!

# 3. Factorial!!!!
def factorial(nber): # National Bereau of Economic Research (nber)
    if nber == 0:
        return 1
    else:
        return nber * factorial(nber - 1) # Recursion :)

print(factorial(3)) # Sehr gut

# 4. Mean calculator
# Tempting to create a class, but I will fall in line with the task...

def meanIT(numbers: list, meanType: str = "arithmetic") -> float:
    if meanType == "arithmetic":
        return mean(numbers)
    elif meanType == "geometric":
        prod = 1
        
        for n in numbers:
            prod *= n
        n = len(numbers)
        
        return prod**(1/n)
    
    elif meanType == "harmonic":
        reciprocal = 0
        count = 0
        
        for n in numbers:
            if n > 0:
                reciprocal += 1/n
                count += 1

        if count > 0:
            return count / reciprocal
        else:
            return None
    else:
        return None

# Recall the numbers list:
numbers = [1, 2, 3, 0, -10, 14, 3]
numbers2 = [1, 2, 3, 1, 10, 14, 3]

print(f"Ari mean: {meanIT(numbers)}")
print(f"Geo mean: {meanIT(numbers, 'geometric')}")
print(f"Harmoni: {meanIT(numbers, 'harmonic')}")
# Looks fine

print(f"Geo mean: {meanIT(numbers2, 'geometric')}")
print(f"Harmoni: {meanIT(numbers2, 'harmonic')}")
# Clean

        
    
    




































