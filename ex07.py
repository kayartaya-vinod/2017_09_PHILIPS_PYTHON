#  working with JSON data and files

filename, content = "people.json", ""

with open(filename, encoding="utf-8") as fh:
	for line in fh:
		content += line

import json

data = json.loads(content) # list of dicts

# list of only names
names = [ d["first_name"] + " " + d["last_name"] for d in data] 
print(names)

print("-"*75)


for d in data:
	print("%s %s is from %s" % 
		(d["first_name"], d["last_name"], d["city"]))

print("-"*75)


for d in data:
	print("%(first_name)s %(last_name)s is from %(city)s" % d)












