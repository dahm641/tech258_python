single = 'single'
double = "double"

print(single)
print(double)

good_string = "I said \"wow\" and then i left"
print(good_string)

Hw = "Hello World!"

print(len(Hw))
print(Hw[0])
print(Hw[-1])
print(Hw[-2])
print(Hw[:3])
print(Hw[5:-2])

#string methods

white_space = "lots of space at the end                                                                                   "
print(len(white_space))
print(white_space.strip())
print(len(white_space.strip()))


#count subtring within string
example_string = "text within a text"
print(example_string.count("text"))

#make a string upper case
print(example_string.upper())

#lowercase
print(example_string.lower())

#captilize
print(example_string.capitalize())

#replace
print(example_string.replace("text", "replacement"))

#concatenation and casting

a = "here "
b = "more "
c = "much more"

print(a + b + c)

x = 2
y = 5.4
z = " theres now a number 25.4 unless we put a space in"
w = "30"

print(str(x) + " " + str(y) + z)
print (x + y + int(w))

# F-strings

name = "lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm} cm tall")

#can manipulate

name = "snoopy"
years = 52

print(f"{name.upper()} IS {years*7} IN DOG YEARS")

pi = 3.14159265359

print(f"{pi.__round__(3)}")
print(f"{pi.__round__(5)}")
print(f"{pi:.3f}") #different method
print(pi.__round__(5))
