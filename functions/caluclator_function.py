from calculator_operators import *

def calculator ():

# asking a user what operation they would like to use and then checking it to see if its valid, if not then try again
     user_status = True
     while user_status:

         user_input = input("Hello! please choose the operation you would like to use \n press 1 for '+' \n press 2 for '-' \n press 3 for '/' \n press 4 for '*' \n")
         if user_input.isdigit() and int(user_input) <= 4:
             user_status = False
         else:
             print(f"Sorry I don't understand '{user_input}' , Please enter a valid character!")


# asks for numbers to add using the relevant function then checks the input using other functions created earlier
     if user_input == "1":

         user_numbers = input("Enter the numbers you'd like to add, separated by spaces: \n")

         while is_valid_input(user_numbers) is False:

             print(f'"{user_numbers}" is not a valid option try again')
             user_numbers = input("Enter the numbers you'd like to add, separated by spaces: \n")

         print("The sum is:", addition(user_numbers))


     elif user_input == "2":
         user_numbers = input("Enter the numbers you'd like to subtract, separated by spaces: \n")

         while is_valid_input(user_numbers) is False:
             print(f'"{user_numbers}" is not a valid option try again')
             user_numbers = input("Enter the numbers you'd like to subtract, separated by spaces: \n")

         print("The total is:", subtraction(user_numbers))

     elif user_input == "3":
         user_numbers = input("Enter the numbers you'd like to divide, separated by spaces: \n")

         while is_valid_input(user_numbers) is False:
             print(f'"{user_numbers}" is not a valid option try again')
             user_numbers = input("Enter the numbers you'd like to divide, separated by spaces: \n")
         print("The total is:", division(user_numbers))

     elif user_input == "4":
         user_numbers = input("Enter the numbers you'd like to multiply, separated by spaces: \n")

         while is_valid_input(user_numbers) is False:
             print(f'"{user_numbers}" is not a valid option try again')
             user_numbers = input("Enter the numbers you'd like to multiply, separated by spaces: \n")
         print("The total is:", multiplication(user_numbers))
