# # Inside the editor, complete the following steps:


# # 1.Create a class called Person
class Person:
    
# # 2.Add an __init__ method that takes name and age as parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

# # 3.Add a method called greet that prints "Hello, my name is " followed by the name
    def greet(self):
        print(f"Hello, my name is {self.name}")

# # 4.Create an object p1 of the class with name "John" and age 36
p1 = Person("John", 36)

# # 5.Call the greet method on p1
p1.greet()


# class Car:
#   def __init__(self, brand):
#     self.brand = brand
#   def show(self):
#     print(self.brand)

# # Create an object
# c1 = Car("Ford")
# # Call the show method
# c1.show()
