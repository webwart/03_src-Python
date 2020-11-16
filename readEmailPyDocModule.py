#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 16-11-2020
#    Goals: Understand eMail Module and parse email files from uberspace
#      Ref: https://docs.python.org/3/library/email.examples.html
#      Ref: 
#      Ref: 
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs with eMail as string , runs with eMail as file from überspace
#       >N: --


# Import the email modules we'll need
from email.parser import BytesParser, Parser
from email.policy import default

# If the e-mail headers are in a file, uncomment these two lines:
# with open(messagefile, 'rb') as fp:
#     headers = BytesParser(policy=default).parse(fp)

messagefile = "TestEmailFromOlbersUberspace.txt"

with open(messagefile, 'rb') as fp:
    headers = BytesParser(policy=default).parse(fp)

#  Or for parsing headers in a string (this is an uncommon operation), use:
'''
headers = Parser(policy=default).parsestr(
        'From: Foo Bar <user@example.com>\n'
        'To: <someone_else@example.com>\n'
        'Subject: Test message\n'
        '\n'
        'Body would go here\n')
'''

#  Now the header items can be accessed as a dictionary:
print('To: {}'.format(headers['to']))
print('From: {}'.format(headers['from']))
print('Subject: {}'.format(headers['subject']))

# You can also access the parts of the addresses:
print('Recipient username: {}'.format(headers['to'].addresses[0].username))
print('Sender name: {}'.format(headers['from'].addresses[0].display_name))