# --------------- send email in Python ---------------
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s
To: %s
Subject: %s

%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo() # extended helo (hello)
        server.starttls() # TLS: transport layer security
        server.login(gmail_user, gmail_pwd)

        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except Exception as err:
        print "failed to send mail", err

def main():
    email = "kayartaya.vinod@gmail.com"
    import getpass
    password = getpass.getpass("Enter password for %s: " % email)

    print("Sending the email....")

    send_email(email, password, "vinod@knowledgeworksindia.com", "Testing via Python", "Hello\nThis is a test mail\n\nVinod.")


if __name__ == '__main__':
    main()

# --------------- send email in Python ---------------
