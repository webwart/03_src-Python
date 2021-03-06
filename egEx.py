#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: -- First: --
#    Goals: Learn RegEx
#      Ref:
#      Ref: https://docs.python.org/3.8/howto/regex.html
#      Ref: 
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --


## Metacharacters
# Most letters and characters will simply match themselves. There are exceptions to this rule; some characters are special "metacharacters", and don’t match themselves.
# . ^ $ * + ? { } [ ] \ | ( )
# If you want to match one of these characters you need to escape them with "\". In python strings "\" is however a special character. Accordingly you need add "\\" for python. 
# Cumbersome: regEx_test = "\\\\rainer" will match "\rainer". 
# The solution is to use Python’s raw string notation for regular expressions;
# Better: regEx_test = r"\\rainer" 


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
