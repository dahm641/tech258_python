## What is scripting

![pcture](https://visionx.io/wp-content/uploads/2023/03/Scripting-Language-vs-Programming-Language-768x768.png)

Scripting is writing a block of code that can automate a process for us. it is useful if we need something done
repeatedly and takes out a lot of the manual labour to keep running scripts.
For example we can write a script that shuts down servers everyday at night time so we don't have to do it every time.
It saves us time. It talks directly to the computer.


A programme is more interactive and helps humans communicate with their computers better. usually for large scale programmes with a broad rang of activities. can be used with compiled or interpreted languages whereas scripts have a very specific task and are usually just interpreted languages. 
## What are packages

Packages are predfined groups of functions that we can call upon to save ourselves from writing extra code. They are made to make our life easier and reduce the amount of coding we need to do with some built in functions.

We can import them from online and other places too if needed. 
this can be done using the `pip` command in the terminal.

An example is:
```python
import datetime
print(datetime.datetime.today())
```
This uses the date time package which gives us some functions to use.
Here I used the function `datetime.today` to get the current date and time.

To get a complete list of builtin functions we can run the following:
```python
for name in dir(builtins):
    if name[0].islower():
       print(name)
```

## Examples of devops python scripts:

1. Automated back up script
2. Server health check script
3. Deployment automation script
4. Infrastructure provisioning script
5. Alert scripts
6. Scaling script
7. Container orchestration script
8. Packaging script
9. Testing script
10. CI/CD pipelin script

### Example of automated back up script:

```python
import shutil
import os
import datetime

def backup(source_dir, target_dir):
    # Create a timestamp for the backup folder name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(target_dir, f"backup_{timestamp}")

    # Create the backup directory
    os.makedirs(backup_dir)

    # Copy files from source directory to backup directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            target_path = os.path.join(backup_dir, os.path.relpath(source_path, source_dir))
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.copy2(source_path, target_path)

    print(f"Backup completed. Files backed up to: {backup_dir}")

# Example usage:
source_directory = "/path/to/source/directory"
target_directory = "/path/to/target/directory"

backup(source_directory, target_directory)

```
### This script does the following:

1. Takes a source directory (the directory to be backed up) and a target directory (where the backup will be stored) as input.
2. Creates a timestamp to use as part of the backup folder name.
3. Creates a backup directory with the timestamp in the target directory.
4. Copies files from the source directory to the backup directory while preserving file metadata (using shutil.copy2).
5. Prints a message indicating that the backup is completed.
