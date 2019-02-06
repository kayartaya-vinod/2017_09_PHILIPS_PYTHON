# working with loops

author_name = "Vinod"
author_email = "vinod@vinod.co"

def factorial(input=5):
	"""
	returns the factorial of the input
	using a simple while loop
	"""

	if type(input)!= int:
		raise ValueError("Only <int> is allowed!")

	f = 1
	while input>1:
		is_prime(input)
		f *= input
		input -= 1

	return f


# dunder members are not accessible 
# when "from <module> import *" is used
def __test_is_prime__():
	n1 = 11
	print("n1 is prime -> ", is_prime(n1))

	n1 = 99
	print("n1 is prime -> ", is_prime(n1))


def __test_factorial__():
	n1 = 10
	f1 = factorial(n1)
	print("Factorial of {} is {}".format(n1, f1))
	f1 = factorial()
	print("Factorial of {} is {}".format(5, f1))
	# f1 = factorial("ten")
	# print("This is the end of script!")


def is_prime(input):
	"""
	returns True if the input is a prime
	else False

	The 'input' must be an <int> value
	"""

	if type(input) != int :
		raise ValueError("Only <int> is allowed!")

	if input<=0:
		raise ValueError("Input must be > 0")

	limit = input//2 + 1
	for d in range(2, limit):
		if input % d == 0:
			return False
	return True


def fac(input):
	if input<=0:
		raise ValueError("Input must be >= 1")
	
	if input==1:
		return 1
	
	return input * fac(input-1)

def __test_fac__():
	import sys
	# sys.setrecursionlimit(12000)
	n = 100
	f = fac(n)

	print("Factorial of {} is {}".format(n, f))

if __name__ == '__main__':
	__test_fac__()

















