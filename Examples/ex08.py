"""
Convert an input CSV file into a JSON file

1st line in the CSV is used as the keys for the JSON/dict
"""

def main():
	csv_filename = input("Enter the CSV filename: ")
	json_filename = input("Enter the JSON filename: ")
	csv2json(csv_filename, json_filename)
	print("JSON saved to the file '{}'".format(json_filename))

def csv2json(csv_filename, json_filename):
	lst = list()
	with open(csv_filename, encoding="utf-8") as fd:
		keys = fd.readline().strip().split(",")
		for line in fd:
			values = line.strip().split(",")
			d = dict(zip(keys, values))
			lst.append(d)

	with open(json_filename, "wt") as fd:
		import json
		fd.write(json.dumps(lst))

if __name__ == '__main__':
	main()
