#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn dealing with files
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------

pathOnHos = "C:\\Users\\Public\\01_data\\"

try:
    file = open(pathOnHos + "testData.txt", 'r')
except IOError:
    print("the file myfile does not exist!!!")
file.seek(0)
file.read

for line in file:
    print(line)

file.close
