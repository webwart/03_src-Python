#!/user/  .in Unix only

#  ------------------------------------
#  Porject: Instracen mailing list
#   Author: Rainer Warth
#  Version: 31-03-2020
#    Goals: Sent eMails for InTraCen survey
#      Ref: https://realpython.com/python-send-email/   
#      Ref: 
#      Ref: 
#      Ref: 
#    Satus: <runs> - <bug> (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: eMail does not arrive at rainer.warth@hotamil.ch 
# Funcions: make connection to server , read csv file with eMails , send message with attachement 
#       >N: Remove Attachement and add HTML text. 
#  ------------------------------------


# -*- coding: utf-8 -*-

#  Prod: eu-service-export@warth-sapiens.com
#  .> ssh webwarts@wolf.uberspace.de

import email, smtplib, ssl , csv , argparse

from email  import encoders
from email.mime.base import  MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Data for the connexion (socket)
smtp_server = "wolf.uberspace.de"
port = 587  # For starttls
# password = input("Type your password and press enter: ")
password = "JcXwg8WW5-Irr5_eMra-5ra_Eu3er5xp"   # keepass 

# Data for eMail
sender_email = "eu-service-export@warth-sapiensio.com"
receiver_email = "eu-service-export@warth-sapiensio.com"  # Enter receiver address
subject = "EU Untersuchung - Handelshindernisse und Informationsbedarf für Dienstleistungsexporteure im IKT- und Bausektor"
body = "--"

parser = argparse.ArgumentParser()
parser.add_argument("eMailFile" , help="Read eMails from InTraCen.csv file")
args = parser.parse_args()
print(args.eMailFile)



#Create a multipart message and set headers
# message = MIMEMultipart("alternative")
message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email   # I do use a .csv file
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to eMail
# message.attach(MIMEText(body, "plain"))


'''
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
'''


# text = message.as_string()



# Create the plain-text and HTML version of your message
text = """\
    Guten Tag,
	meine Firma führt im Auftrag der EU eine Untersuchung zu folgendem Thema durch:

    Handelshindernisse und Informationsbedarf für Dienstleistungsexporteure in den Sektoren Bau- und IKT-Dienstleistungen.

    Die EU hat den Internationalen Trade Centre (InTraCen) in Genf beauftragt die Untersuchung in 15-EU Ländern durchzuführen. InTraCen hat für die Erhebung von Daten in Deutschland meine Firma warth-sapiensIO beauftragt. Sie finden weiterführenden Informationen unter: warth-sapiensio.com/eu-export

    Die EU nutzt die gewonnen Erkenntnisse für Verhandlungen mit nicht-EU Ländern und um Informationsangebote wie «The Market Access Database (MADB)» anzubieten: https://madb.europa.eu/madb/
    Mit dieser Untersuchung kann Ihre Firma der EU mitteilen, wo sie Bedarf im Abbau von Bürokratie und Handelshindernisse sehen. Wer wäre in Ihrer Firma bereit seine Erfahrung mit der Betreuung von Kunden aus nicht-EU Ländern zu berichten?</p>
    Mit freundlichen Grüssen, Rainer Warth
     ----------------------------------------------------------------
    Sind finden mehr Informationen zu der Untersuchung auf unserer Webseite: https://warth-sapiensio.com/eu-export
    Folgende Sektoren und Dienstleistungen werden noch bis zum 9. Mai untersucht:
        - Hoch- und Tiefbau:  Bauen, Umbauen, Renovieren, Verwalten
        - Telekommunikation: Übertragung von Sprache, Daten, Text, Ton, Video.
        - Computer: Softwareentwicklung, Planung von IT, Hosting, Datensammeln, etc.

    -----------------------------------------------------------------
    Rainer Warth, Dr., MBA<br>
    Route de Lausanne,30...............Tel.: +41 21 515 29 01                                   
    1180 ROLLE, Suisse.................https://warth-sapiensio.com/
"""

html = """\
<html>
  <body>
    <p>Guten Tag,<br>
	meine Firma führt im Auftrag der EU eine Untersuchung zu folgendem Thema durch:</p>
    <p><b>Handelshindernisse und Informationsbedarf für Dienstleistungsexporteure in den Sektoren Bau- und IKT-Dienstleistungen.</b></p>
    <p> Die EU hat den Internationalen Trade Centre (InTraCen) in Genf beauftragt die Untersuchung in 15-EU Ländern durchzuführen. InTraCen hat für die Erhebung von Daten in Deutschland meine Firma warth-sapiensIO beauftragt. Sie finden weiterführenden Informationen unter: <a href="https://warth-sapiensio.com/eu-export/">warth-sapiensio.com/eu-export<a></p> 
    Die EU nutzt die gewonnen Erkenntnisse für Verhandlungen mit nicht-EU Ländern und um Informationsangebote wie «The Market Access Database (MADB)» anzubieten: https://madb.europa.eu/madb/  </p>
    <p>Mit dieser Untersuchung kann Ihre Firma der EU mitteilen, wo sie Bedarf im Abbau von Bürokratie und Handelshindernisse sehen. Wer wäre in Ihrer Firma bereit seine Erfahrung mit der Betreuung von Kunden aus nicht-EU Ländern zu berichten?</p>
    <p>Mit freundlichen Grüssen, Rainer Warth</p>
     ----------------------------------------------------------------<br>
     Sind finden mehr Informationen zu der Untersuchung auf unserer Webseite: <a href="https://warth-sapiensio.com/eu-export/">warth-sapiensio.com/eu-export<a><br>
     Folgende Sektoren und Dienstleistungen werden noch bis zum 9. Mai untersucht:<br>
    <ol>
      <li>Hoch- und Tiefbau:  Plannen, Entwerfen, Überwachen, Bauen, Umbauen, Renovieren, Verwalten</li>
      <li>Telekommunikation: Übertragung von Sprache, Daten, Text, Ton, Video.</li>
      <li>Computer: Softwareentwicklung, Planung von IT, Hosting, Datensammeln, etc.</li>
    </ol>
    -----------------------------------------------------------------<br>
    Rainer Warth, Dr., MBA<br>
    Route de Lausanne,30...............Tel.: +41 21 515 29 01<br>                                    
    1180 ROLLE, Suisse.................https://warth-sapiensio.com/<br>


  </body>
</html>
"""



# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

text = message.as_string()

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
#    with open("contacts_file.csv") as file:
#   I used this file to test the programm: 0001-0008_BusinessRegister-Email-Test.csv
#    with open("0001-0008_BusinessRegister-Email-Test.csv") as file:
#   
#      with open("0001-0010_BusinessRegister-Email.csv") as file:
#

    with open(args.eMailFile) as file:

        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip header row
# ID;telephone;phoneRAI;website;Response;Comments;email_1;sector;company
#        for name, receiver_email, grade in reader:
        for indi , telephone , phoneRAI , website , response , comments , receiver_email , sector , company  in reader:

            server.sendmail(
                sender_email,
                receiver_email,
                # message.format(name=name,grade=grade),
                text,
            )
            print("{};{};{};{};{};{};{};{};{}".format(indi , telephone , phoneRAI , website , response , comments , receiver_email , sector , company ))

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 