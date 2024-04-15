import os

# Directory
directory = "test_dir"

# parent directory
parent_directory = "D:/sparta global/"

# path
path = os.path.join(parent_directory, directory)

# filename
filename = "test_file.txt"

# filepath
filepath = os.path.join(path, filename)

# create the file
with open(filepath, "w") as file1:
    toFile = "Contents of the file go here"
    file1.write(toFile)
print(f"File {filename} has been created in {filepath} with contents: {toFile}")

