# python standard library
# consists of many modules and added to python by default

import random
import math
import os
import sys
import datetime
import builtins
import requests

# random demo

# print(random.random())
# print(random.randrange(1, 10))

# math demo

# num_float = 23.66
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(math.pi)
# print(f"remainder from 1/5 {math.remainder(1, 5)}")

# os demo

# # returning current working directory
# working_dir = os.getcwd()
# print(f"current working directory is: {working_dir}")
#
# # get current user
# username = os.environ.get("USERNAME") or os.environ.get("USER")
# print(f"username is: {username}")
#
# # cpu cores
# cpu_cores = os.cpu_count()
# print(f"cpu cores is: {cpu_cores}")
#
# # make directory
# os.mkdir("test_dir")


# # sys demo
# print(f"current path is {sys.path}")
# print(sys.version)

# date time demo
print(f"todays date is {datetime.datetime.today()}")

# # built ins demo
#
# for name in dir(builtins):
#     if name[0].islower():
#         print(name)

# requests demo
requests_bbc = requests.get("https://www.bbc.co.uk/")
print(requests_bbc.status_code)
print(requests_bbc.content)
print(requests_bbc.links)
