import requests
import json

json_body = json.dumps({"postcodes": ["PR30SG", "M456GN", "EX16 5BL"]})

headers = {"Content-Type": "application/json"}

# request post needs headers and body

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
print(post_multi_req.json())

# data= -> accepts a string (so we had to use json.dumps first)
# json= -> accepts a python dictionary
