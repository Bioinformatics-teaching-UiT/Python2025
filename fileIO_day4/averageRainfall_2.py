import os
os.chdir("Day4")

# Reading the rainfall file and creates a list with the lines
lines = []
with open("rainfall.txt", "r") as file:
    for line in file:
        lineSplit = line.strip().split() # Splits up the line: month and float value as new elements
        if len(lineSplit) == 2:
            month, value = lineSplit
            lines.append((month, value))

# Writing the monthly file
with open("rainfallMonths.txt", "w") as file: # Note: w (write) instead of r (read)
    for month, value in lines:
        file.write(f"The average rainfall in {month} was {value}.\n")

# Superb










