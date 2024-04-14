# calculator

def addition(numbers):
    # Split the input string by spaces and convert each part to an integer
    numbers_list = [float(num) for num in numbers.split()]
    return sum(numbers_list)

def subtraction(numbers):
    # Split the input string by spaces and convert each part to an integer
    numbers_list = [float(num) for num in numbers.split()]
    return numbers_list[0] - sum(numbers_list[1:])

def division (numbers):
    # Split the input string by spaces and convert each part to an integer
    numbers_list = [float(num) for num in numbers.split()]
    result = 1 # sets result as 1
    for every_number in numbers_list[1:]:
        result *= every_number # shorthand for result = result * every_number
    return numbers_list[0] / result # divide first number by multiplication of rest of numbers

def multiplication (numbers):
    # Split the input string by spaces and convert each part to an integer
    numbers_list = [float(num) for num in numbers.split()]
    result = 1
    for every_number in numbers_list:
        result = result * every_number # shorthand for result = result * every_number
    return result

#creating a function to check if numbers inputted as string can be converteed into a float
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# creating a function that uses the is_number function to check multiple inputs
def is_valid_input(input_string):
    # Split the input string by spaces
    numbers = input_string.split()

    # Check if each part is a valid number
    # each iteration of num is going thorugh each of the numbers inputted and cheking that they are numbers.
    # whilst they are numbers it keeps going if its not then it returns false and stops the loops
    for num in numbers:
        while is_number(num) is not True:

            if is_number(num) is True:
                return True
            else:
                return False


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


calculator()

# def addition(numbers):
#     # Split the input string by spaces and convert each part to an integer
#     numbers_list = [int(num) for num in numbers.split()]
#     # Sum up the numbers
#     result = sum(numbers_list)
#     return result

# print("Enter the numbers you'd like to add, separated by spaces:")
# user_numbers = input()
# print("The sum is:", addition(user_numbers))
