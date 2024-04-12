# calculator

def addition(*multipleargs):
    return sum(multipleargs)

def subtraction(*multipleargs):
    return multipleargs[0] - sum(multipleargs[1:])

def division (*multipleargs):
    result = 1
    for every_number in multipleargs [1:]:
        result = result * every_number
    return multipleargs[0] / result

def multiplication (*multipleargs):
    result = 1
    for every_number in multipleargs:
        result = result * every_number
    return result


#
# def calculator ():
#
#      user_status = True
#
#      while user_status:
#          user_input = input("Hello! please choose the operation you would like to use \n press 1 for '+' \n press 2 for '-' \n press 3 for '/' \n press 4 for '*' \n")
#          if user_input.isdigit() and int(user_input) <= 4:
#              user_status = False
#          else:
#              print("Please enter a valid character!")
#
#
#      if user_input == "1":
#         print("what numbers would you like to add today?")
#         user_number = input()
#         print(addition(user_number))
#
#      elif user_input == "2":
#         print("what numbers would you like to subtract today?")
#         user_number = int(input())
#         print(subtraction(user_number))
#
#      elif user_input == "3":
#         print("what numbers would you like to divide today?")
#         user_number = int(input())
#         print(division(user_number))
#
#      elif user_input == "4":
#         print("what numbers would you like to subtract today?")
#         user_number = int(input().split())
#         print(multiplication(user_number))
#
# calculator()