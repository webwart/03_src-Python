#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-08-2020 Previous: -- First: --
#    Goals: Learn Use of SQL databases , Read array of objects from json file
#      Ref: https://www.codeproject.com/tips/4067936/Load-JSON-File-with-Array-of-Objects-to-SQLite3-On
#      Ref:  
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --

import json
import sqlite3
from datetime import datetime

db = sqlite3.connect('myDB.sqlite')

with open('sql_json.json' , encoding='utf-8-sig') as json_file:
    json_data = json.loads( json_file.read())

print(json_data)