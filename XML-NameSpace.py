#!/user/  .in Unix only
# PYTHON.org Documentation.
# 20.5.1.7. Parsing XML with Namespaces
#
# https://docs.python.org/3/library/xml.etree.elementtree.html
# \TestData\XML\xmlNamespaces.xml
#
# see also http://www.python-kurs.eu/python_XML_SAX.php
# A powerful python library is 
# http://lxml.de/

import xml.etree.ElementTree as ET

pathOnHos = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\XML\\"
# pathOnHos = "C:\\Users\\Public\\Documents\\Pub_CodeDev\\TestData\\XML\\"

try:
    file = open(pathOnHos + "xmlNamespace-actor.xml", 'r')
except IOError:
    print("the file myfile does not exist!!!")
    
for line in file:
    print(line)
    

tree = ET.parse(pathOnHos + "xmlNamespace-actor.xml")
root = tree.getroot()
print("-----------")
print(root.tag)
print(root.attrib)

for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)

print("--Better way / create dictionary ---------")

ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
    for char in actor.findall('role:character', ns):
        print(' |-->', char.text)
