#!/user/  .in Unix only
"""
#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 05-12-2020 Previous: 06-04-2020 "refactor use Data_Test First: 06-04-2020
#    Goals: os, pathlib, shutil module to deal with files and directories.
#      Ref: https://realpython.com/working-with-files-in-python/
#      Ref: https://realpython.com/python-pathlib/
#      Ref: https://www.youtube.com/watch?v=IWDC9vcBIFQ&t=23s -> Creates a file search engine with GUI
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
"""

import os
from pathlib import Path

# Using the OS module works like this:
with os.scandir('Data_Test/') as entries:
    for entry in entries:
        print(entry.name)


print("-----" * 7)
print("Using the pathlib is the prefered way.")
print("Listing files and directories")
print("-----" * 7)

entries = Path('Data_Test/')
for entry in entries.iterdir():
    print(entry.name)

print("-----" * 7)
print("Listing files in an directory")
print("-----" * 7)
# List all files in directory using pathlib
basepath = Path('Data_Test/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)


print("-----" * 7)
print("Listing sub-directories")
print("-----" * 7)
# List all subdirectory using pathlib
basepath = Path('Data_Test/')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)

print("-----" * 7)
print("Getting file attributes")
print("-----" * 7)
current_dir = Path('Data_Test')

for path in current_dir.iterdir():
    info = path.stat()
    print(info.st_mtime)