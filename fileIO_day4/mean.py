# I had some problems with the directory. Hence:
import os
os.chdir("Day4") # Day4 is the current folder. May need to be removed on your PC. 

# --- Method 1 ---
# Opening the file
file = open("numbers.txt", "r")
# Read the lines, convert to floats and storing them in a list
numbers = []
for line in file.readlines(): numbers.append(float(line.strip()))

file.close()

mean = sum(numbers) / len(numbers)

print(f"Mean: {round(mean,2)}")

# --- Method 2 ---
with open("numbers.txt", "r") as file:
    numbers = []
    for line in file.readlines(): numbers.append(float(line.strip()))

mean = sum(numbers) / len(numbers)
print(f"Mean: {round(mean,2)}")















