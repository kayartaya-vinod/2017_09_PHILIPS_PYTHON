# numutils.py

# Utility function to convert number to words

def num2words(num):

	if type(num) != int:
		raise ValueError("Only <int> allowed")

	if num>999999999:
		raise ValueError("Max allowed is 99,99,99,999")

	units = ",one,two,three,four,five,six,seven,eight,nine,ten,eleven,tweleve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty".split(",")
	tens = ",,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety".split(",")
	others = ",hundred,thousand,lakh,crore".split(",")

	arr = []
	count = 0
	while num>0:
		if count==1:
			arr.append(num%10)
			num //= 10
		else:
			arr.append(num%100)
			num //= 100
		count += 1

	result = ""
	count -= 1
	while count>=0:
		n = arr[count]

		if n==0: 
			count -= 1
			continue
		
		if n<=20:
			result += units[n] + " "
		else:
			a = n%10
			b = n//10
			result += tens[b] + " "+ units[a] + " "

		result += others[count] + " "
		count -= 1

	return result

def main():
	in_words = num2words(1029374)
	print(in_words)
	in_words = num2words(10001)
	print(in_words)
	in_words = num2words(123456789)
	print(in_words)

if __name__ == '__main__':
	main()

