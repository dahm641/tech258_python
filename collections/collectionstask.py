starters = ["nachos", "chicken wings", "olives", "breadsticks"]
mains = ["steak", "burger", "lobster", "curry"]
desserts = ["ice cream", "cake","pie"]

# create a list of prices
price_starters = [3.99, 6.99, 2.99, 1.89]
price_mains = [16.50, 9.99, 24.99, 12.99]
price_desserts = [3.89, 4.89, 4.19]

# convert prices into dictionaries with th mains being the key and prices being value

price_starters = zip(starters, price_starters)
price_starters = dict(price_starters)

price_mains = zip(mains, price_mains)
price_mains = dict(price_mains)

price_desserts = zip(desserts, price_desserts)
price_desserts = dict(price_desserts)

# greet customer and ask for order


print(f"Hello, welcome to the python resteraunt. Here are our starters today {starters}")
print("what would you like?")
starter = input()

print(f"our mains are {mains} what would you like")
mains = input()

print(f"our desserts are {desserts} what would you like")
dessert = input()

# displays order and price rounded to 2dp

print(f"your order is {starter} with {mains} and {dessert} \n your order total is {round(price_starters[starter] + price_mains[mains] + price_desserts[dessert],2)}")



