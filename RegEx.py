#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: -- First: --
#    Goals: Learn RegEx
#      Ref: https://docs.python.org/3.4/howto/regex.html
#      Ref:  
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --

import re
lines = ['555-1212', 'ILL-EGAL', '@Article{2007Azambuja,']
for test_string in lines :
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, ' --> is a valid US local phone number')
    else:
        print (test_string, ' --> rejected')
        
print("------match-----")
# Match takes an entire string/line. Therefore, ^ does not work or makes sense
for test_string in lines :
    if re.match(r'^@Article{2007Azambuja,', test_string):
        print(test_string, ' --> Is a valid BIB haeder')
    else:
        print (test_string, ' --> rejected')

print("------search---")
# Here the ^@ works since search goes through all the characters

for test_string in lines :
    if re.search(r'^@Article{2007Azambuja,', test_string):
        print(test_string, ' --> Is a valid BIB haeder')
    else:
        print (test_string, ' --> rejected')
