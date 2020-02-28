#  Author: Rainer Warth
#  Description: Programm to find CHUV numbers
#  Learn how use Dictionaries
#  Ref: Python Docs Tutorial 5.5

# HOS at Chuv (End 160216)
# pathOnHos = "C:\\Users\\rwarth\\Documents\\Pub_CodeDev\\TestData\\"
# Amalfi
pathOn = "C:\\Users\\Public\\01_data\\"

tableDictio = {}

try:
    file = open(pathOn + "150430_GridData_CHUV.txt", "r")
                
except IOError:
    print("the file myfile does not exist!!!")
    exit
    
for line in file:
    listPosCode = line.split(":")
    print(listPosCode[0])
    print(listPosCode[1])
    tableDictio[listPosCode[0]] = listPosCode[1]

file.close
WantedPosition = input("What position: ")
print(tableDictio[WantedPosition])

      
# print(tableDictio)


'''
tableDictio = {"A1":"BNZR", "A2":"ZVPX", "A3":"KEHW"}
print(tableDictio["A1"])
# Add a new valua pair
tableDictio["A4"] = "MEHC"
print(tableDictio)
'''
