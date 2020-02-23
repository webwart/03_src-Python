
#!/user/  .in Unix only
#
# -open Ecb.xml file
# -get currency and value relative to EURO
# -get date
# -make  line with <date> <value Dollar> <value rubel> ....
# -save line into file with date in the name. yymmdd_ForexTo1Euro_ECB

# https://docs.python.org/3/library/xml.etree.elementtree.html
# 20.5.1.2. Parsing XML

import xml.etree.ElementTree as ET

pathOnHos = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\XML\\"
# pathOnHos = "C:\\Users\\Public\\Documents\\Pub_CodeDev\\TestData\\XML\\"

try:
    file = open(pathOnHos + "eurofxref-2015-08-27.xml", 'r')
except IOError:
    print("the file myfile does not exist!!!")
    
for line in file:
    print(line)

file.close

tree = ET.parse(pathOnHos + "eurofxref-2015-08-27.xml")
root = tree.getroot()
print("-----------")
print(root.tag)
print(root.attrib)
print("-----------")
for child in root:
    print(child.tag,      child.attrib)
print("-----------")
print(root[0].tag,root[0].attrib)
print(root[1].tag,root[1].attrib)
#print(root[2][0][0].tag,root[2][0][0].attrib)
print(root[2][0][0].attrib)
print(root[2][0][0].get("currency"))
print(root[2][0][0].get("rate"))


#>N: In need to find out what element.get element.find exactly do

print("----cube loop-------")

lineRate = ""   # empty string
lineRateList = []  # empty list
whiteSpace = " ; "

    
for cube in root.findall('{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube'):
    curency_Name = cube.findall('{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube')
    # print(curency_Name)
    for cur_cube in curency_Name:
        currencyLevel = cur_cube.findall('{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube')
        #currencyLeve.get("time")
        
#    rate = cube.get('rate')
        # print(currencyLevel)
        for cur_rate in currencyLevel:
            cur_rate.get("time")
            print(cur_rate.get("currency"), cur_rate.get("rate"))
            lineRate = lineRate + whiteSpace + cur_rate.get("rate")
            lineRateList.append(cur_rate.get("rate"))

print(lineRate)
print("----print from list-------")
print("<>".join(lineRateList))


    

