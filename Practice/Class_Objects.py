# # Python Classes/Objects

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

# Create Object
# Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)

# Delete Objects
# Delete the p1 object:

del p1
print("Object p1 is deleted here...")

# Multiple Objects
# Create three objects from the MyClass class:
print("Creating multiple objects here and printing them....")
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print("p1->",p1.x)
print("p2->",p2.x)
print("p3->",p3.x)
# Note: Each object is independent and has its own copy of the class properties.


# The pass Statement
# class definitions cannot be empty,
# if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error.

class Person:
  pass
