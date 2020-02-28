# >A: Rainer Warth
# >D: Learn to use the xml, pathlib, and panda library to create graph with x-rates EUR, USD, UKP, JPY
# >R: https://pathlib.readthedocs.org/en/pep428/
# >R: https://docs.python.org/3/library/pathlib.html?highlight=pathlib#module-pathlib
# >R: 20.5.1.7. Parsing XML with Namespaces
# >R: ttps://docs.python.org/3/library/xml.etree.elementtree.html
# >R: See also work done with ExbXmlToCSV.py
# >D: created 13-06-2016 , version 24-09-2019
# >N: Understand Pure versus concret clases e.g. PureWindowsPath <-> WindowsPath
# Two flavors are supported: Windows and POSIX (all other)
#


from pathlib import Path
import xml.etree.ElementTree as ET

#
# Listing subdirectories from the directory, where this file is stored
#
print("::: List subdirectories :::")
p = Path('C:\\Users\\Public\\01_data\\ECB-ExRates')
print([x for x in p.iterdir() if x.is_dir()])


print("::: List subdirectories :::")
file_xml_list = [file_xml for file_xml in p.iterdir() if file_xml.is_file()]
for file in file_xml_list:
        print(file.name)





#
# Listing Python source files in this directory tree, where this file stored)
#
print("\n::: Python source file :::")
print(list(p.glob('**/*.txt')))
q = list(p.glob('**/*.txt'))



#
# Navigating inside a directory tree
# >NOTE: This is not the solution shown in the doc.
# print("\n::: Navigating inside a directory tree :::")
# q = p / "SpyderTutorial\\hello.py"   #Works, but might not be standard
# print(q)
# print(q.resolve())

#
# Quering path properties
#
print("\n::: File exists, Is directory :::")
print(p.exists())
print(p.is_dir())

#
# Opening file (see L-TextFileOpen.py for other ways)
#
print("\n::: Opening a file (version 1):::")

with q[1].open() as f: 
        print(f.name)
        tree = ET.parse(f)
        root = tree.getroot()
        print("-----------")    
        print(root.tag)
        print(root.attrib)
        print("-----------")
        for child in root:
                print(child.tag,      child.attrib)
        print("-----------")
        print(root[0].tag,root[0].attrib)
        print(root[1].tag,root[1].attrib)
        #print(root[2][0][0].tag,root[2][0][0].attrib)
        print(root[2][0][0].attrib)
        print(root[2][0][0].get("currency"))
        print(root[2][0][0].get("rate"))
        f.close()

