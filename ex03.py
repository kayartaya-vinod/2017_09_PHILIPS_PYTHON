# working with 
# 1. conditional statements
# 2. Indentation
# 3. Keybaord input


if __name__ == '__main__':
	# Python 2 will return a raw value (int, float etc)
	# Python 3 will return <str>
	num = int(input("Enter a number: "))

	if (num % 2 == 0):
		print("The number was divisible by 2")
		print("Hence it is an even number")
	else:
		print("Unable to divide the number by 2")
		print("Hence it is an odd number")

