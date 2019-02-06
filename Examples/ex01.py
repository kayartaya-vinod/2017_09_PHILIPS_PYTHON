#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 

# This is our first python script
# This one just prints a Hello message

print("This is the start of ex01.py")
print("The name of this module for Python is:", __name__)

message = "Hello, World"

print(message)

name = 'Martin'
age = 33

print("Name =", name, "and ", end="")
print("Age =", age, "years")

print("Result of concatenation...")
s1 = "Name = " + name
print(s1, "and ", end="")

s2 = "Age = " + str(age) + " years"
print(s2)
print("This is the end of ex01.py")