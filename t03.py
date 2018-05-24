### ----------- Mongodb Client Example -----------

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.get_database("mywork")
contacts = db["contacts"]

name = input("Enter name: ")
city = input("Enter city: ")

p1 = {"name": name, "city": city}
contacts.insert_one(p1)

for c in contacts.find():
	print(c["name"], c["city"], sep=", ")

print("Done!")

### ----------- Mongodb Client Example -----------
