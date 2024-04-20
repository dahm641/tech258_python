# Dictionaries

# Key value pairs
# key is the reference, value is the data

student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up"],
    "number": [3, 5, 12]
}

print(student1["stream"])
print(student1["completed_lesson_names"][0])
student1["completed_lessons"] = 3
student1["completed_lesson_names"].append("tuples")
print(student1["completed_lesson_names"])
print(student1.keys())
print(student1.values())



# Example dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30}

# Calculate total
total_sum = sum(my_dict.values())
print("Total sum:", total_sum)

print("sum is:", sum(student1["number"]))
