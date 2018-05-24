import requests

url = "http://kelutral.com/rest/contacts.php"

resp = requests.get(url, params={"id": 56}, headers={"Content-Type": "application/json", "WrittenBy": "Vinod", "ReadBy": "You"})
print(resp.json())
print(resp.headers)
print(resp.request.headers)

# new_data = dict()
# new_data["first_name"] = "Shyam"
# new_data["last_name"] = "Sundar"
# new_data["email"] = "shyamsundar@mail.com"
# new_data["phone"] = "9888997779"
# new_data["city"] = "Bangalore"
# new_data["dob"] = "1972-10-02"

# resp = requests.post(url, json=new_data)
# print("response status_code = ", resp.status_code)
# print("response text = ", resp.text)