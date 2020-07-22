#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn to write to a file.
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------

#!/user/  .in Unix only
#
# -This file is to Generate a test file, which can be copied into the SBP Wordpress installation.
# 
'''
pathOnHos = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\"
# pathOnHos = "C:\\Users\\Public\\Documents\\Pub_CodeDev\\TestData\\XML\\"

try:
    file = open(pathOnHos + "150915_SBB-BiobankTest.txt", 'w' )
except IOError:
    print("the file myfile does not exist!!!")

for i in range(1001):
    print("line" + str(i))
    file.write("line")

'''

pathOnHos = "C:\\Users\\Public\\1_data\\TestData\\"


file = open("newfile.txt", "w")

file.write("1 -hello world in the new file\n")

file.write("2 -and another line\n")
'''
for i in range(1001):
    #print("line" + str(i))
    file.write("line")
'''
firstString = "I am the first string"
firstString =   firstString +  " another string"

file.write(firstString)

file.close
print("done")

'''

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


#>>> Inned to find out what element.get element.find exactly do

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

'''
    

