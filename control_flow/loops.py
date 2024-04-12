# TASK 2
# examples of different loops used in different scenarios

# examples 1

print(f"\n{'=' * 60}")
print(f"{'*' * 16}Embedded lists and dictionaries{'*' * 16}")
print(f"{'=' * 60}")

# given data

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# prints first list doubled
# 1. Under the starter code, write a loop to print double each number in the list "list_data"

print(embedded_lists[0][2])

# 2. Write another loop on the next line, this one should print items inside of the "embedded_lists"
# The output should be:
# [1, 2, 3]
# [4, 5, 6]
for i in list_data:
    print(2*i)

# 3. Create another loop inside of the "embedded_lists" for loop to list each individual item in each list.
# Output should be:
# [1, 2, 3]
# 1
# 2
# 3
# [4, 5, 6]
# 4
# 5
# 6

for i in embedded_lists:
    print(i)
    for x in i:
     print(x)

# 4. Write a new loop on a new line. This one should loop through the dictionary "dict_data".
# The output should be:
# 1
# 2
# 3

for i in dict_data:
    print(i)

# 5. Write another loop, this time it should use the built-in dictionary method value() to print each value for each key inside the dictionary

for data in dict_data.values():
    print(data)

# 6. Copy and paste your last loop on a newline. Create an embedded loop (loop inside the loop you pasted) to extract and print the values within the dictionary of each item WITHIN THAT dictionary.
# Here is the expected output:
# Bronson
# $0.05
# Masha
# $3.66
# Roscoe
# $1.14

for data in dict_data.values():
    for value in data.values():
        print (value)

# 7. Write another loop to loop through the dictionary "dict_data", but this time only print out the money values.
# The output should be:
# $0.05
# $3.66
# $1.14

print("\n")
print("\n")


for dict_items in dict_data.values():
    print(dict_items.get("money"))

# 8. Write one final loop. This loop should loop through the items in "list_data" and include a nested (indented) if statement inside the loop so that each loop will check the number it is currently on to see if:
#
# - if the number is less than 3, it prints 'less than 3'
#
# - if the number equals 3, it prints 'I found three'
#
# - if the number is greater than 3, it prints 'greater than 3'
# The output should be:
# less than 3
# less than 3
# I found three
# greater than 3
# greater than 3

print("\n")

for d in list_data:
    x = d
    if x < 3:
        (
            print("less than 3")
        )
    elif x == 3:
        (
            print("i found 3")
        )
    else:
        (
            print("more than 3")
        )

# TASK 3
print(f"\n{'=' * 60}")
print(f"{'*' * 16}Iterative loop{'*' * 16}")
print(f"{'=' * 60}")

# Create a while loop that loops while x is less than 10. Everytime the loop completes it should:
#
# - Print the value of x to the screen in an f-string
#
# - Increment (add 1 to x)
#
# So the output should be:
#
# print x -> 0
# print x -> 1
# print x -> 2
# print x -> 3
# print x -> 4
# print x -> 5
# print x -> 6
# print x -> 7
# print x -> 8
# print x -> 9
#
#
#
# Once your code works, comment out the assignment of the "x" variable. What happens?
#
# Write a brief comment stating what would happen if you didn't increment x each time loop completes (would the while loop ever stop?)
#
# Add something to your loop so that it breaks out of the loop if "x" > 4

x = 0

while x < 10:
    print(f"x is {x}")
    x += 1

    if x > 4:
        break
# Task 4: Improving existing code with control flow
#
# 1. Loop until age is all digits
#
# Look at this code:
#
# # Ask user for their age
# age = input("What is your age? ")
#
# print(f" Your age is {age}")
#
#
#
# The problem with this code is that even if the user is 20, they could enter "20" or "twenty". Let's standardise the input to get the age as digits...
# Hints:
# To check is 'age' is all digits, use the 'age' string's method .isdigit()
#
# 2. Only accept valid input


print(f"\n{'=' * 60}")
print(f"{'*' * 16}Get and validate a users age{'*' * 16}")
print(f"{'=' * 60}")

user_prompt = True

while user_prompt:
    age = input("what is your age? ")
    # input is alwas a string
    if age.isdigit() and int(age) <= 117:
        user_prompt = False
    else:
        print("please provide answer in digits, below 117")

print(f"your age is {age}")