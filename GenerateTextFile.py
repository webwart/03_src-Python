#!/usr/bin/python

# Open a file in write mode
fo = open("foo.txt", "w+")
print ("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

str = "This is 6th line"
# Write a line at the end of the file.
line = fo.write( str )

# Now read complete file from beginning.

for index in range(6):
   print ("Line No ", index)
   str2 = ("no ")
   fo.write( str2 )

# Close opend file
fo.close()
print("--done---")
