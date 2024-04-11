# lists

# collections are a way to store multiple pieces of data in one reference/object
# lists are the most common/simplest collection

# lists are known as arrays in other languages

# print the list to a new line
shopping_list = ["oranges", "coffee", "bread", "eggs", "milk", "crisps"]
print("this is your shopping list: \n" + str(shopping_list)) # \n means new line

# print data type
print("The data type of your shopping list is: \n" + str((type(shopping_list))))

# print first item
print("the first item in your lsit is " + shopping_list[0])

# print last item
print("the first item in your lsit is " + shopping_list[-1])

# change second item to rice
print("the second item in your list is " + shopping_list[1])
shopping_list[1] = "rice"
print("second item is now " + shopping_list[1])

# add forgotten items to list
forgotten_items = ["toffee", "coffee"]
shopping_list.extend(forgotten_items)

# add item to end of list
print("length of list is currently", len(shopping_list))
shopping_list.append("carrots")
print("carrots have now been added. new shopping list length is now ", len(shopping_list))
print("this is your shopping list: \n" + str(shopping_list)) # \n means new line

# remove something from anywhere in list
shopping_list.remove("bread")
print("this is your shopping list: \n" + str(shopping_list)) # \n means new line

# remove last item (or any item without reference
shopping_list.pop()
print("last item has been removed, this is your shopping list: \n" + str(shopping_list)) # \n means new line

# remove first item
shopping_list.pop(0)
print("first item has been removed, this is your shopping list: \n" + str(shopping_list)) # \n means new line

# add item to start
shopping_list.insert(0, "watermelon")
print("watermelon has been added to the start, this is your shopping list: \n" + str(shopping_list)) # \n means new line

