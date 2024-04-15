
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