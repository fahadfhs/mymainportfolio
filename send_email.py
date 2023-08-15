import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "fahadhussainshaikh1@gmail.com"
password = "owwufqgrgzkkkjkh"

receiver = "fahadfhs95@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Check up
Hi!
How are you?
Bye!
"""
# context = contex because we are being explicit, as the order of argument gets messed up
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
