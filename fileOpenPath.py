#!/user/  .in Unix only

pathOnHos = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\"

try:
    file = open(pathOnHos + "testData.txt", 'r')
except IOError:
    print("the file myfile does not exist!!!")
    
for line in file:
    print(line)

file.close

