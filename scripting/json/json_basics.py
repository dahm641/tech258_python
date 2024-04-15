import json

car_data = {
    "name": "tesla",
    "engine": "electric"
}

print(type(car_data))
# Created a python dictionary

# json.dumps() --> serialises json to a formatted string

car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))
# converted it to a JSON STRING. JSON NEEDS TO BE STRING.

# json.dump() --> creates a stream object and expects a file object to write to. It makes it into a file.

with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)