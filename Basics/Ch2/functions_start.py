# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def fun():

#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# fun()

# function that takes parameters
# def fun(greeting):

#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# fun("How are you doing")

# function that returns a value
# def cube(x):
#   return x*x*x

# result = cube(3)
# print(result)

# function with default value for an parameter
# def fun(greeting, name = None):

#   print("hello world!")
#   if name == None:
#    name = input("What is your name? ")
#   print(greeting, name)

# fun("Nice to meet you, ")


# function with variable number of parameters
def multiadd(start, *args):
  result = start
  for x in args:
    result = result + x
  return result

print(multiadd(10, 4, 8, 11, 33, 1, 6))  