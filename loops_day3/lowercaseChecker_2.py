
# Checking if there are any lowercase chars in the string
def lowercaseChecker(string: str) -> str:
    lower = []
    for chara in string:
        if chara.islower():
            lower.append(chara)
    if len(lower) > 0:
        print("Lowercase characters:")
        print(lower) # Prints as a list
    else:
        print("No lowercase characters found!")

string = "JHBjhbhjfbhjbsJHBJUB IGBHUBN hjbhsbd JHB" # Fingerbased randomizer (no seed indeed ;))

lowercaseChecker(string)

# May be useful to use a set if you want to avoid duplicates




