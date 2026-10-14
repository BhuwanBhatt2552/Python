# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
# x = 10/0
# print(x)

# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# try:
#   x = 10 / 0
# except:
#   print("division by zero is not defined")

# You can also catch specific exceptions
try:
  answer = input("what should I divide 10 by?")
  num = int(answer)
  print(10/num)
except ZeroDivisionError as e:
  print("you cannot divide any number by zero")
except ValueError as e:
  print("you have not entered a valid number")
  print(e)
finally:
  print("Finally always works")