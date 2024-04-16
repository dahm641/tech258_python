import sys, os, json, yaml
def load_json() -> dict:
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            file = open(sys.argv[1], "r")
            data = json.load(file)
            file.close()
            print("JSON is valid.")
            return data
        else:
            print(f"no file found with name {sys.argv[1]}")
    else:
        print("Please provide a json file name as 2nd argument.")




def create_yaml(data: dict) -> json:
    filename = sys.argv[1].split(".")[0] #filename matching original json file

    with open(f"{filename}.yaml", "w") as yaml_file:
        yaml.dump(data, yaml_file, sort_keys=False) # to keep the same order yaml.dump has a sort_keys keyword argument that is set to True by default. Set it to False to not reorder:
    print("file converted successfully!")

# def main() -> None:
#
#     # Check if given a file name as an argument.
#     if len(sys.argv) > 1:
#         if os.path.exists(sys.argv[1]):
#             json_dict = load_json(sys.argv[1])
#             create_yaml(json_dict, sys.argv[1])
#
#     # If not, convert all JSON files in json_files.
#     else:
#         files = os.listdir("./json_files")
#         print(files)
#         for file_name in files:
#             json_dict = load_json(file_name, "./json_files")
#             create_yaml(json_dict, file_name, "./yaml")
#
# if __name__ == "__main__":
#     main()



#storing returned value from json
json_2_dict = load_json()

#putting that value into the next function creating a yaml
create_yaml(json_2_dict)
