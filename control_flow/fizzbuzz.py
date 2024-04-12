# make a fizzbuzz game to print numbers 1 to 100
# multiples of 3 print fizz multiples of 5 is buzz multiples of 3 and 5 is fizzbuzz

x = 1

while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print ("FizzBuzz")
    elif x % 3 == 0:
        print ("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else: print(x)
    x += 1
