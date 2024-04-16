import sys
import os
import json
import yaml


def load_json(file_name: str, path: str) -> dict:
    """Takes a file_name returns a dict from JSON."""
    path = os.path.join(path, file_name)

    if os.path.exists(path):
        file = open(path, "r")
        data = json.load(file)
        file.close()
        print("JSON is valid.")
        return data
    else:
        print(f"no file found with name {file_name}")


def write_yaml(data: dict, file_name: str, path) -> None:
    """Takes a dictionary and writes as yaml to given file name."""
    # Create a file name matching the json file given as sys.argv[1]
    file_name = file_name.split(".")[0]

    yaml_path = os.path.join(path, file_name)
    with open(f"{yaml_path}.yaml", "w") as file:
        yaml.dump(data, file, sort_keys=False)
        print(f"successfully written to {yaml_path}.yaml")


def main() -> None:

    # Check if given a file name as an argument.
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            json_dict = load_json(sys.argv[1])
            write_yaml(json_dict, sys.argv[1])

    # If not, convert all JSON files in json_files.
    else:
        files = os.listdir("./json_files")
        print(files)
        for file_name in files:
            json_dict = load_json(file_name, "./json_files")
            write_yaml(json_dict, file_name, "./yaml")

if __name__ == "__main__":
    main()