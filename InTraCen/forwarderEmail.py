#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 20-03-2020
#    Goals: Learn use smtplib and email module. I want to send eMails for the InTraCen project.
#      Ref: https://realpython.com/python-send-email/   
#      Ref: 
#      Ref: 
#      Ref: 
#    Satus: <runs> - <bug> (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs 
# Funcions: make connection to server , read csv file with eMails , send message with attachement 
#       >N: Check /rakawas/users/forward , Can I send to rainer.warth@hotmail.ch , Add InTraCen ID to header. 
#  ------------------------------------


# -*- coding: utf-8 -*-
import email, smtplib, ssl , csv

from email  import encoders
from email.mime.base import  MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Data for the connexion (socket)
smtp_server = "olbers.uberspace.de"
port = 587  # For starttls
# password = input("Type your password and press enter: ")
password = "JcXwg8WW5-Irr5_eMra-5ra"   # keepass 

# Data for eMail
sender_email = "forwarder@rainer-warth.eu"
receiver_email = "rainer.warth@gmail.com"  # Enter receiver address
subject = "10:39 An email with attachment from Python"
body = "This is an email with attachment sent from Python"


#Create a multipart message and set headers
# message = MIMEMultipart("alternative")
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to eMail
message.attach(MIMEText(body, "plain"))

filename = "DATASET-EU-ServiceExport.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()



# Create the plain-text and HTML version of your message
# see - Including HTML Content -

# Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
# part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
# message.attach(part1)
# message.attach(part2)


# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
'''
context = ssl.create_default_context()
with smtplib.SMTP_SSL( smtp_server , port , context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
'''

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
#    server.sendmail(sender_email, receiver_email, message.as_string())
#    server.sendmail(sender_email, receiver_email, text)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, receiver_email, grade in reader:
            server.sendmail(
                sender_email,
                receiver_email,
                # message.format(name=name,grade=grade),
                text,
            )
            print(receiver_email)

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 