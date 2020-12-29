#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-12-2020
#    Goals: Learn the use of selenium to drive Firefox with geckodriver
#      Ref: https://pypi.org/project/selenium/
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: Test the other example code from the pypi web-site
#  ------------------------------------


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://seleniumhq.org/')