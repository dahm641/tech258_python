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

# KEYWORD ARGUMENTS
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#
# If you do not know how many keyword arguments that will be passed into your function:
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

fruits = ["apple", "banana", "cherry"]
def my_function(food):
  for x in food:
    print(x)

my_function(fruits)

# Return Values
# To let a function return a value, use the return statement:

