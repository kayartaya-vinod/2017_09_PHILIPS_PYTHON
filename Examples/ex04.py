"""
Module: ex04

Author: Vinod Kumar Kayartaya <vinod@vinod.co>
Version: 1.0
"""
# Working with user defined function

# define the function
def say_hello(name="World", char="*"):
	"""
	prints a decorated greeting message

	Parameters: 
	1 -> a name 
	2 -> a character symbol
	"""
	print(char*50)
	print(char*3, end="")
	print("Hello, {} ".format(name).center(44), end="")
	print(char*3)
	print(char*50)
	print()

# execute this section only if this is the main module
if __name__ == '__main__':
	# call the function
	say_hello("Vinod Kuamr")
	say_hello(char="~")
	say_hello(char="#", name="Vinay")
	say_hello(name="Shyam Sundar", char=".")
	say_hello("John Doe", "^")