from twilio.rest import Client

account = "AC63ad713eafda99301ed6026efbc9ce0c"
token = "f2156934847391a1c67a181c302ec8a3"

client = Client(account, token)


# client.messages.create(from_="+91 97314 24784", to="+91 98440 83934", body="Ahoy! This is Vinod!")

numbers = client.available_phone_numbers("IN").local.list()
for n in numbers:
	print(n)