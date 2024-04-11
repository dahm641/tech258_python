# Bools and None

a = True
b = False

print (a == b)
print (a != b)
print (a >= b) #true
print (a <= b) #false

# False is always 0!

hi ="Hello World"
print(hi.isalpha())
print(hi.islower())
print(hi.isupper())
print((hi.endswith("d")))
print(hi.startswith("H"))

# can use these checks to make decisions

print(bool("a")) # always true unless empty
print(bool())

# any number other than 0 is true

print(bool(0))
print(bool(-5))

# None is an object that is a place holder has no type
# None as a bool is false
# None != False
