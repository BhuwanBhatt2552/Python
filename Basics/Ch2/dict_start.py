# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydict = {
  1:"hello",
  2:"what",
  3: 25091,
  4:9587658939,
  'one':"bhuwan",
  5.5: 201584651

}
# print(mydict)

# dictionaries are accessed via keys
# print(mydict["one"])
# print(mydict.get(5.5))

# you can also set dictionary data by creating a new key
# mydict[8] = 'its my birthday'
# print(mydict[8])
# print(mydict)

# Trying to access a nonexistent key will produce an error
# print(mydict[9])

# To avoid this, you can use the "in" operator to see if a key exists
# print("one" in mydict)
# print("my" in mydict)

# You can retrieve all of the keys and values from a dictionary
# print(mydict.keys())
# print(mydict.values())

# You can also iterate over all the items in a dictionary
for key, val in mydict.items():
  print(key, val)