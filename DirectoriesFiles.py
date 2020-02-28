#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Obtain Lists of directories and files
#      Ref: http://www.diveintopython.net/file_handling/os_module.html
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------ 

import os

# PROD: walk through directories on Windows \SBP-In\

print("Start now")
os.path.join("c:\\music\\ap\\", "mahadeva.mp3")

# create list/directory filled with directory name and file name

# dirRoot = os.listdir ("C:\\Users\\rwarth\\Documents\\SBP-Next\\150513_Director-SBP\\i-Applications")
dirRoot = os.listdir ("C:\\Users\\Public\\01_data")


# pathOnHos = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\"
# pathHosToTestEndRef = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\EndnoteJabRef\\"
print(len(dirRoot))   # Number of files/direcgories in Root directory



# NumLinesInFile = 0


# make a copy of bibtex and save (add times stamp)
# opend bibtex file and add data from dirEndPDFlist
# 

# try:
#     file = open(pathHosToTestEndRef + "BiblioFocusBiobank-Test.bib", 'r')
# except IOError:
 #   print("the file myfile does not exist!!!")
    
# for line in file:
#    print(line)

# >>>   Defien RegEx:     beginning of line,@,Article/Book,{,numbers characters,","
# See the LearnRegEx.py program in Pub-CodeDev\Python   
#     NumLinesInFile = NumLinesInFile + 1

# file.close
# print("The file contains:   ")
# print(NumLinesInFile)




# check Whitfield Endnote entry and JabRef, see TestData

