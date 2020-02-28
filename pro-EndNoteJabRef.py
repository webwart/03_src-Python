# description: EndnoteJabRef 
# author: Rainer Warth
# data: 09.08.2015
# DEV: Testdata \Pub_CodeDev\TestData\EndnoteJabRef\
# PROD:
import os

# PROD: walk through directories on Windows \SBP-In\
# read directory name and file name in the directory
# Ref: http://www.diveintopython.net/file_handling/os_module.html
print("Start now")
os.path.join("c:\\music\\ap\\", "mahadeva.mp3")

# create list/directory filled with directory name and file name

dirEndPDFlist = os.listdir ("C:\\Users\\rwarth\\Documents\\SBP-Biblio\\150210_FocusBiobanking.Data\\PDF")
# pathOnHos = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\"
pathHosToTestEndRef = "C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\TestData\\EndnoteJabRef\\"
NumLinesInFile = 0


# make a copy of bibtex and save (add times stamp)
# opend bibtex file and add data from dirEndPDFlist
# 

try:
    file = open(pathHosToTestEndRef + "BiblioFocusBiobank-Test.bib", 'r')
except IOError:
    print("the file myfile does not exist!!!")
    
for line in file:
    print(line)

# >>>   Defien RegEx:     beginning of line,@,Article/Book,{,numbers characters,","
# See the LearnRegEx.py program in Pub-CodeDev\Python   
    NumLinesInFile = NumLinesInFile + 1

file.close
print("The file contains:   ")
print(NumLinesInFile)

# >Next: change and save file, check Whitfield Endnote entry and JabRef, see TestData
, add
