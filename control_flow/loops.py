list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

print(embedded_lists[0][2])


for i in list_data:
    print(2*i)

for i in embedded_lists:
    print(i)
    for x in i:
     print(x)

for i in dict_data:
    print(i)

for data in dict_data.values():
    print(data)

for data in dict_data.values():
    for value in data.values():
        print (value)
        
for dict_items in dict_data.values():
    for value in dict_items.values():
        print(value)

print("\n")
print("\n")


for dict_items in dict_data.values():
    print(dict_items.get("money"))

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





