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



def calculator ():

     user_status = True


     user_input = input("Hello! please choose the operation you would like to use \n press 1 for '+' \n press 2 for '-' \n press 3 for '/' \n press 4 for '*' \n")
     if user_input.isdigit() and int(user_input) <= 4:
         user_status = False
     else:
         print("Please enter a valid character!")


     if user_input == "1":
         print("Enter the numbers you'd like to add, separated by spaces:")
         user_numbers = input()
         print("The sum is:", addition(user_numbers))


     elif user_input == "2":
         print("Enter the numbers you'd like to subtract, separated by spaces:")
         user_numbers = input()
         print("The total is:", subtraction(user_numbers))

     elif user_input == "3":
         print("Enter the numbers you'd like to divide, separated by spaces:")
         user_numbers = input()
         print("The total is:", division(user_numbers))

     elif user_input == "4":
         print("Enter the numbers you'd like to multiply, separated by spaces:")
         user_numbers = input()
         print("The total is:", multiplication(user_numbers))

     else:
        print(f" {user_input} is an invalid input. Please enter a valid number (1, 2, 3, or 4) or 'q' to quit.")

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
