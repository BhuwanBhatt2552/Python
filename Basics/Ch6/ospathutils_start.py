#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import time
from datetime import datetime

# Print the name of the OS
print(os.name)

# Check for item existence and type
print("Item Exists:", path.exists("test.txt"))
print("Item is File:", path.isfile("test.txt"))
print("Item is a directory:", path.isdir("test.txt"))

# Work with file paths
print("Items path : ", path.realpath("test.txt"))
print("Item's path and name : ", path.split(path.realpath("test.txt")))

# Get the modification time
t = time.ctime(path.getmtime("test.txt"))
print(t)
print(datetime.fromtimestamp(path.getmtime("test.txt")))

# Calculate how long ago the item was modified
td = datetime.now() - datetime.fromtimestamp(path.getmtime("test.txt"))
print(f"It has been {td} since the file is been modified")
print(f" or, {td.total_seconds()} seconds")