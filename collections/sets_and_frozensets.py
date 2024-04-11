# sets and frozen sets

# create a set

fruits = {"apple", "banana", "cherry"}
print(fruits)

# sets are UNORDERED and UNINDEXED (random order)

# add element
fruits.add("orange")
print(fruits)

# remove an element
fruits.remove("apple")
print(fruits)

# attempt to add a duplicate
# NO DUPLICATES in a set
fruits.add("banana")
print(fruits)

# can convert a list into a set to remove duplicates
example = [1, 2, 3, 1]
no_dupes = set(example)
print(no_dupes)

example2 = {1, 2, 3, 4, 5, 6}
print(example2)

# frozen set is just an immutable set

frozen_set = frozenset(["hello", "world"])
print(frozen_set)

# frozen_set.add("abc") gives error



