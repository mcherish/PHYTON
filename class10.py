tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
i'll do a list:
\t* Cat food
\t* Fishes
\t* Caatnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("how old are you?",end='')
age = input()

print(f"so, you are {age} old...")