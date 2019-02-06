# Accept numbers and print the total

def main():
	total = 0

	while True:
		val = input("Enter a number (0 to stop): ")
		try:
			num = int(val)
		except Exception as e:
			print(e)
			print("Invalid input, only numbers are allowed.")
		else:
			if num==0: break 
			total += num
		finally:
			print("Try more!")
		
	print("The sum of inputs is", total)


if __name__ == '__main__':
	main()