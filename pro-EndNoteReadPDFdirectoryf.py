#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: 09-08-2015 First: 09-08-2015
#    Goals: Learn walk directory and regEx
#      Ref: https://pathlib.readthedocs.org/en/pep428/
#      Ref: https://docs.python.org/3/library/pathlib.html?highlight=pathlib#module-pathlib
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: broken
#       >N: --


from pathlib import Path

# PRODUCTION file5
# 

# TEST files:
# - Amalfi -
# Dev. PathDir = "C:/Users/Public/Documents/Pub_CodeDev/TestData/EndnoteJabRef"
# Pro. PathDir = "C:/Users/raine_000/Documents/SBP-Biblio/150210_FocusBiobanking.Data/PDF"
#
# - Ascona -
#  PathDir PathDir = "C:/Users/raine_001/Documents/SBP-Biblio/150210_FocusBiobanking.Data/PDF")
#
# - Milano -
#

# PathDir = "C:/Users/Public/Documents/Pub_CodeDev/TestData/EndnoteJabRef"


PathDir = "C:/Users/raine_000/Documents/SBP-Biblio/150210_FocusBiobanking.Data/PDF"

print("---Start EndNoteReadPDFdirectory---")
DictioDirPDF = {}
p = Path(PathDir)
for DirName in p.iterdir():
    if DirName.is_dir():
        print(DirName.name)
        for FileName in DirName.iterdir():
            if FileName.exists(): 
                DictioDirPDF[DirName.name] = FileName.name
                print("\\__" + DirName.name + "--" + FileName.name)
            else:
                print("does not exist")
    else:
        print(DirName.name + "--> not a directory")

for directory, file  in DictioDirPDF.items():
    print("Directory %s has the file %s" % (directory, file))


# >Next:    a) Make a function which returns the DictioDirPDF.
#           b) Test results of import of BIBTEX and ALL file from Endnote  C:\Users\rwarth\Documents\SBP-Biblio\TestExports\
#           c) Install new JabRef and test import of standard Endnote file.

    
