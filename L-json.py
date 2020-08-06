#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 03-08-2020
#    Goals: learn usage of json module
#      Ref: https://realpython.com/python-json/
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------ 

import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


'''
UTNIL: Note that dump() takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.

I can use a list of dictionaries and the module provides nicely formatted json output.

'''

with open("data_file_indent4.json", "w") as write_file:
    json.dump(data, write_file, indent=4 )