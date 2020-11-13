#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn pathlib
#      Ref: https://pathlib.readthedocs.org/en/pep428/
#      Ref: https://docs.python.org/3/library/pathlib.html?highlight=pathlib#module-pathlib
#      Ref: https://pbpython.com/pathlib-intro.html
#      Ref: https://www.btelligent.com/blog/best-practice-arbeiten-in-python-mit-pfaden-teil-1/
#      Ref: https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
#	   Ref: https://realpython.com/python-pathlib/
#      Ref: http://www.python-kurs.eu/python3_dateien.php -> shows how to read line by line or all at once and then access a line.
#      Ref: see 07_JobWorkspace/ReadJobLinkFile.py
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------


# Date: 31.01.2016
# Pure versus concret clases e.g. PureWindowsPath <-> WindowsPath
# Two flavors are supported: Windows and POSIX (all other)
#
# 11.1.1 Basic use
# Import the main class

from pathlib import Path

#
# Listing subdirectories from the directory, where this file is stored
#
print("::: List subdirectories :::")
p = Path('.')
print([x for x in p.iterdir() if x.is_dir()])

#
# Listing Python source files in this directory tree, where this file stored)
#
print("\n::: Python source file :::")
print(list(p.glob('**/*.py')))

#
# Navigating inside a directory tree  NOTE- This is not the solution shown in the doc.
# 

print("\n::: Navigating inside a directory tree :::")
q = p / "SpyderTutorial\\hello.py"   #Works, but might not be standard
print(q)
print(q.resolve())

#
# Quering path properties
#
print("\n::: File exists, Is directory :::")
print(q.exists())
print(q.is_dir())

#
# Opening file (see L-TextFileOpen.py for other ways)
#
print("\n::: Opening a file (version 1):::")
with q.open() as f: 
	print(f.readline())
f.close()
