import requests

postcodes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(postcodes_req)
# print(postcodes_req.content)
#
# print(postcodes_req.json())

data_dict = postcodes_req.json()["result"]
print(data_dict)
print(data_dict["region"])