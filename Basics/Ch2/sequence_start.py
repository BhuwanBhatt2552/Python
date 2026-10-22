# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [ 0, 10, "two", 3.2, False ]
# print(len(mylist))


# to access a member of a sequence type, use []
# print(mylist[2])
# print(mylist[-1])
# mylist[0] = 10
# print(mylist)


# add a list to another list
# otherlist = [2,3,4,5]
# mylist = mylist + otherlist
# print(mylist)


mystr = "This is a string"
# print(mystr[3])


# use slices to get parts of a sequence
# print(mylist[::2])


# you can use slices to reverse a sequence
# print(mylist[::-1])


# Tuples are like lists, but they are immutable
mytuple = (1, 2, 3, "four")
# print(mytuple[2])


# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 4, 5, "hello"}
# print(myset)


# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error :- 'set' object is not subscriptable

# Test for membership
print(1 in mylist)
print(3 in mytuple)
print("hello" in myset)
print("is " in mystr)