

import sys, os, json, yaml

# print(f"This is the name of the program: {sys.argv[0]}")
#
# print(f"Number of elements including the name of the program: {len(sys.argv)}")
#
# print(f"Number of elements excluding the name of the program: {(len(sys.argv) - 1)}")
#
# print(f"Argument List: {str(sys.argv)}")

if len(sys.argv) > 1: # do we have more than one argument?
    if os.path.exists(sys.argv[1]): # is the a filename given actually there
        file = open(sys.argv[1], "r")
        json_file = json.load(file)
        file.close()
        print("JSON is valid")
        print(type(json_file))


    else:
        print(sys.argv[1] + " not found")

else:
    print("Usage: python check_json.py <file>")


