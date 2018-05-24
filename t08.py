import smtplib, getpass

email_from = "kayartaya.vinod@gmail.com"
email_to = "vinod@knowledgeworksindia.com"
subject = "Sending an email from Python"
body = """Hey there!

This is a test mail from Python's smtplib module.

Just ignore it,
and delete it.

Regards,
Vinod.
"""

message = """From: {}
To: {}
Subject: {}

{}""".format(email_from, email_to, subject, body)

password = getpass.getpass("Enter password for {}: ".format(email_from))
try:
	server = smtplib.SMTP("smtp.gmail.com", 587)

	server.ehlo()
	server.starttls()
	server.login(email_from, password)

	server.sendmail(email_from, email_to, message)
	server.close()
	print("Message sent successfully!")
except Exception as err:
	print(err)

