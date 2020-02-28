#!/user/  .in Unix only
# Reference: http://www.python-kurs.eu/python3_dateien.php
#            Shows how to read line by line or all at once and then access a line
#            Shows how to save a Data. Explains pickle module. 
# Description: Demonstration of pathlib use to open a file . The file content is then filtered with regEx.
# Author: Rainer Warth
# Date:   05.02.2016
# >NEXT: -How to deal with more than one RegEx term. (e.g search for line 5: and 10:).
#        - Save to a new file the results.
#        - Open and search several files.
#       - When to use readlines(), readline(), or not all as in  -3-
#

import re
from pathlib import Path

regExNumber = r"5:*."
PathDir = "C:/Users/Public/Documents/Pub_CodeDev/TestData/150916_Lines.txt"

p = Path(PathDir)

# -1-
# Opening file (version 1)
#
print("\n::: Opening a file (version 1):::")

try:
    with p.open() as f: print(f.readline())
    f.close()
except IOError:
   print(p.name, " cannot be found!") 

# -2-
# Opening file (version 2)
# 
print("\n::: Opening a file (version 2):::")
try:
    f = p.open()
    print(f.readline())
    f.close()
except IOError:
   print("the file myfile does not exist!!!")

# -3-
# Apply RegEx to lines using only p.open
# 

try:
    file = p.open('r') 
    for line in file:
        if re.match(regExNumber, line):
            print(line)
        else:
            print("-")
    file.close
except IOError:
    print("the file myfile does not exist!!!")
    
# -4-
# Testing of readlines()
#
f = p.open()
fcontent = f.readlines()
print(fcontent)
print("-"*10)
linecounter = 0
for  line in fcontent:
    linecounter = linecounter + 1
    print(linecounter, "->" ,line)

