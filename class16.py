from sys import argv

script,filename = argv
print(f"We're going to eraser{filename}.")
print("If you don't want that, hit ctrl-c.")
print("If you do want that, hit return")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file. Goodbye!")

target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("lien 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()