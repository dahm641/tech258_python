# Dictionaries

# Key value pairs
# key is the reference, value is the data

student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up"]
}

print(student1["stream"])
print(student1["completed_lesson_names"][0])
student1["completed_lessons"] = 3
student1["completed_lesson_names"].append("tuples")
print(student1["completed_lesson_names"])
print(student1.keys())
