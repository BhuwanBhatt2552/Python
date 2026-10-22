#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
f = open("Demo.txt", "r")
if f.mode == "r":
    # use the read() function to read the entire file
#    content = f.read()
#    print(content)
    files_lines = f.readlines()
    for line in files_lines:
        print("\n",line)