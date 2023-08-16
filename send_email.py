import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "fahadhussainshaikh1@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "fahadhussainshaikh1@gmail.com"
    context = ssl.create_default_context()

    # context = contex because we are being explicit, as the order of argument gets messed up
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
