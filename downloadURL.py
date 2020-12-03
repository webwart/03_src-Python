#!/user/  .in Unix only
# -*- coding: utf-8 -*-

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: -- First: --
#    Goals: Learn Urllib
#      Ref: 
#      Ref:  
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: bub
#       >N: --



###  <<> the script runs, but nothing is saved in the 151229_python.html

# save-webpage.py

import urllib.request

with urllib.request.urlopen('http://www.python.org/') as f:
    print(f.read(400).decode('utf-8'))
    content = f.read(400).decode('utf-8')
    print ("-" * 10)
    print (content)

    f = open('151229_python.html', 'w')
    f.write(content)
    type(f)
    f.close


#---
# f = open('151229_About_swissbiobanking.html', 'w')
# f.write(response)
# f.close

