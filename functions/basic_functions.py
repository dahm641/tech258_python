# Functions
# Purpose?:
# DRY - Don't Repeat Yourself!

##############################

# Function with no arguments

def print_something():
    print("something has been printed")
    # it's been defined but won't run unless its called


# call it below
print_something()


# with an argument it would be
def print_name(name):
    print("hello my name is " + name)


print_name("Dan")


def addition(int1, int2):
    return int1 + int2


# return stores the output otherwise it wont work

print(addition(3, 7))


# Default arguments

def default_addition(int1=2, int2=3):
    return int1 + int2


print(default_addition())


# Multiple arguments

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)


# type hints (what expect output)
def division(num: int, denom: int) -> float:
    return num / denom


print(division(3, 6))
