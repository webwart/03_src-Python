#!/user/  .in Unix only
# PYTHON.org Documentation.
# 20.5.1.2. Parsing XML
# https://docs.python.org/3/library/xml.etree.elementtree.html
# \TestData\XML\country_data.xml
#
# see also http://www.python-kurs.eu/python_XML_SAX.php
# A powerful python library is 
# http://lxml.de/


from bs4 import BeautifulSoup
import urllib
import urllib.request
url1 = ("https://www.reddit.com")
url = ("http://www.python.org")
f = urllib.request.urlopen('http://www.python.org/')
redditHtml = f.read().decode('utf-8')



'''
url = ("https://www.reddit.com")
redditFile = urllib.request.urlopen(url)
redditHtml = redditFile.read()
redditFile.close()
'''

soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))

