#This one is like your scripts with argv
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")

#Ok,that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

#This just takes one argument
def print_one(arg1):
    print(f"arg1:{arg1}")

#This is one takes no arguments
def print_none():
    print("I  got nothin.")

print_two("first","second")
print_two_again("first again","second again")
print_one("just one")
print_none()
