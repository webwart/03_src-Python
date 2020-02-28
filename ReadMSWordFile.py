'''
Description: Test programm to use the docx package
Source:     e-book "Do borring things withpyhton" chapter 13
PyVersion:	3.4
Date:		04.04.2016
>DO:
'''

import docx
doc = docx.Document('demo.docx')

# doc = docx.Document("C:\\Users\\Public\\Documents\\Pub_CodeDev\\TestData\\160407_MSWordFiles\\n-160415_Verwaltungsleiter_MPI-Freiburg\\n-160415_All-Verwaltungsleiter_MPI-Freiburg.docx")

print(len(doc.paragraphs))
