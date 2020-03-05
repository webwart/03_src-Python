#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: -- First: --
#    Goals: Learn XML
#      Ref: https://docs.python.org/3/library/xml.etree.elementtree.html
#      Ref: PYTHON.org Documentation. 20.5.1.2. Parsing XML 
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: broken
#       >N: --




# \TestData\XML\country_data.xml
#
# see also http://www.python-kurs.eu/python_XML_SAX.php
# A powerful python library is 
# http://lxml.de/


import xml.etree.ElementTree as ET
from pathlib import Path

PathDirHos = "C:/Users/rwarth/PUB-Documents/Pub_CodeDev/TestData/XML/country_data.xml"
# pathOnHos = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\XML\\"
# pathOnHos = "C:\\Users\\Public\\Documents\\Pub_CodeDev\\TestData\\XML\\"
# country_data.xml

p = Path(PathDirHos) 

try:
    file = p.open('r')
except IOError:
    print("the file myfile does not exist!!!")
    

for line in file:
    print(line)

# file.close   --> moved to end

tree = ET.parse(file.name)
# tree = ET.parse(pathOnHos + "country_data.xml")


root = tree.getroot()
print("-----------")
print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0].tag,root[0].attrib)
print(root[1].tag,root[1].attrib)

print(root[0][1].text)

# 20.5.1.3. Pull API for non-blocking parsing
# I did not do this part

# 20.5.1.4. Finding interesting elements
# iterate recursively

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

print("--- for loop ")

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

#> 20.5.2 XPATH example
print("--- Xpath --- ")


# Top-level elements
RootList = (root.findall("."))



# All 'neighbor' grand-children of 'country' children of the top-level
# elements
countryList = root.findall("./country/neighbor")
for countryElement in countryList:
    print(countryElement.attrib)
    print("-<>-")

# Nodes with name='Singapore' that have a 'year' child
nodesSingapore = root.findall(".//year/..[@name='Singapore']")
for nodeSing  in nodesSingapore:
    print(nodeSing.attrib)
    print("-*-")
    
# 'year' nodes that are children of nodes with name='Singapore'
nodesYear = root.findall(".//*[@name='Singapore']/year")
for cur_nodeYear in nodesYear:
    print(cur_nodeYear.text)
    print("-:-")

# All 'neighbor' nodes that are the second child of their parent
nodesNeighbor = root.findall(".//neighbor[2]")
for cur_nodeNeighbor in nodesNeighbor:
    print(cur_nodeNeighbor.attrib)
    print("-!-")

file.close
