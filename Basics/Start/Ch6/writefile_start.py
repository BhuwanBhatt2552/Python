# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
f = open("Demo.txt","w+")
f.write("\nThis is a sample file!")
f.close()
# Open the file for appending text to the end
f = open("Demo.txt","a+")

# write some lines of data to the file
f.write("\nThis is is some additional data in sample file")
f.write("\nThis is the last line in Demo file")

# close the file when done
f.close()