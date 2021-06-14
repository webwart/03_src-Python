# 

## Goals

1. Learn to use argparse, pathlib, and generate objects.
2. Learn to organise a python project file structure.

## File structure

./rptree_project/
│
├── rptree/
│   ├── rptree.py
│   ├── __init__.py
│   └── cli.py
│
├── README.md
└── tree.py


## Joural

MON  24-05.2012

>N: I did set-up the directory structure and now I need to contineu.
https://realpython.com/directory-tree-generator-python/

WED  25-05-2021
I can now run the stript.


``` text

(py3p8) C:\Users\Public\03_src\python\m-Courses\rptree_project>python tree.py -h      
usage: tree [-h] [-v] [-d] [-o [OUTPUT_FILE]] [ROOT_DIR]

RP Tree, a directory tree generator

positional arguments:
  ROOT_DIR              generate a full directory tree starting at ROOT_DIR 

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d, --dir-only        generate a directory-only tree
  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]
                        generate a full directory tree and save it to a file

Thanks for using RP Tree!
```