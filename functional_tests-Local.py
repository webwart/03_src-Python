#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn functional test
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: broken
#       >N: --
#  ------------------------------------

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('C:\\Users\\rwarth\Documents\\SBP-Biblio\\TestExports\\160204_Island-ShowAllFields.xml')
assert 'IIS Windows' in browser.title
print("Test comleted")
browser = quit()
