#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 01-11-2020
#    Goals: Find a testing strategy, learn using unittest the moducle comes with python and is used in Django Testing Goat.
#      Ref: https://realpython.com/python-testing/
#      Ref: 
#   Ref_By: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: 
#       >N: ference file or .rst file.
#  ---------------------  
 
# Assert is build into python

assert sum([1, 2, 3]) == 6, "Should be 6"

assert sum([1, 1, 1]) == 6, "Should be 6"

assert sum([1, 2, 4]) == 7, "Should be 6"

print("The programm does not run after AssertError")