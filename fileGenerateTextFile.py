#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn writing to files
#      Ref: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: broken
#       >N: - Consilidate with other file....py
#           - Use rather with open('name of file')as f:
#                             read_data = f.read()
#  ------------------------------------

# Open a file in a specific mode
# r =  only read (default)
# w = only writing , an excisting file will be erased)
# a = opens the file for appending, any data written to the file is automatically added to the end.
# r+ = opens the file for reading and writing.


fo = open("foo.txt", "a")
print ("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

str = "This is 6th line\n"
# Write a line at the end of the file.
line = fo.write( str )

# Now read complete file from beginning.

for index in range(6):
   print ("Line No ", index)
   str2 = ("no \n ")
   fo.write( str2 )

# Close opend file
fo.close()
print("--done---")
