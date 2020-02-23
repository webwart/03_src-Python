#!/user/  .in Unix only
try:
    file = open('testData.txt', 'r')
except IOError:
    print("the file myfile does not exist!!!")
file.seek(0)
file.read

for line in file:
    print(line)

file.close
