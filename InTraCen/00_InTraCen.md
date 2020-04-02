

Test: forwarder@rainer-warth.eu
.> ssh rakawas@olbers

Prod: eu-service-export@warth-sapiens.com
.> ssh webwarts@wolf.uberspace.de



## Journal

### WED 18-03-2020

-1- Counting eMail numbers
Total:	9140
Leer	3373
eMails:	5767

-2- eMail with python

RealPython has a guide which reads the eMail adresse from a CSV file.
[CSV-eMail](https://realpython.com/python-send-email/)

Willemer Buch , erklärt auch sockets.
[Sockerts-eMail](http://www.willemer.de/informatik/python/netzwerk.htm)

Anweisung mit Schritt für Schritt Erklärung
[Schrit-eMail](https://codingworld.io/project/e-mails-versenden-mit-python)

Link to qMail, welches bei uberspace eingesetzt wird.
[qmail](https://cr.yp.to/qmail.html)

### FRI 20-03-2020

-1- Calls¦Worksheet
I reorganized my InTraCe files in \RAI-Next\200409_Intracen. I do use the the BusinessRegister_RKW.xlsx file to make calls and to update the results. In this file I have also optimized the order of the columns, removed all ";", -"-, and a lot of commas. 
>N: Create .csv file from \RAI-Next\200409_Intracen\n-200320_BusinessRegister_RKW.xlsx

-2- eMail¦RealPython 
I could successfully apply the scripts from RealPython. I did send via forwarder@rainer-warth.eu a message to r.w@gmail.com
forwarderEmail.py
>N: send to eMails to r.w@gmail.com  , inbox@sapiensio.com , new@.
>N: Work with attachement.

### WED 25-03-2020
-1- uberspace¦spam¦password
I had to reset the password of forward@rainer-warth.eu. 
Ubespace: "Bitte setze mit 'vpasswd forwarder' ein neues, sicheres Passwort". Ich habe jedoch zuerst uberspace mail user password forwarder benutzt.
\keepass\

-2- forwardEmail.py
I can now send eMail to serveral customers. I can also add an attachement.
>N: send to eMails to r.w@gmail.com  , inbox@sapiensio.com , new@.
>N: Work with attachement.
>N: Test MS-Word attachement .docx


### TUE 31-03-2020
-1-     Established eMail accounts
forwarder@rainer-warth.eu
eu-service-export@warth-sapiensIO.com
I did set the TXT record on INXW.com as DNS entry. "Jedoch musst du das "Name"-Feld leer lassen und den "v=spf1 mx ~all"-Wert in "Value" eintragen."

-2-     Wrote python script wsaEmail copy.py 
THe script takes an CSV file and send a HTML text from eu-service-export@warth-sapiensIO.com  on wolf.

-3-     Website¦Data protection.
>N: I need to update my site warth-sapiensIO.com


THU  02-04-2020
-1-  Website¦
I completed Dataprotection and the EU-export page.

-2-  wsaEmail.py
I finished and tested script. I did send the first 100 eMail. I defined the following SP.

>SP: Send Intracen eMail

''' text
OPEN.... VScode
OPEN.... in VScode open 0001-0xxx_BusinessRegister-Email.csv   
OPEN.... in VScode open \RAI-Next\200409_Intracen\SurveyDataCollection\n-200403_eMailBusinessRegister_RKW.csv  ->(2)
FIND.... ----->N:----- in (2) , remove , an place curso at the beginning of the same line
COPY.... lines from cursor to next 29 or 39 lines
INSER... 0001-0xxx_BusinessRegister-Email.csv
OPEN.... in VScode open wsaEMAIL copy.py 
VERIFY.. line 180     with open("0001-0030_BusinessRegister-Email.csv") as file
RUN..... wsaEmail copy.py
SAVE.... print out in InTraCenEmailResults.csv
TYPE.... to each result set the time-stamp: 200402-1515
'''