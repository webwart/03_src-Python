#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn use pandas to find if a vorwahl is in the intracen phone number.
#      Ref: Pandas_Edx.py
#      Ref: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str -> to find() and in Operator.
#      Ref: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files -> reading/writing files to text or json format. 
#      Ref: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences -> list , tuples , 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------


# -*- coding: utf-8 -*-


import numpy as np 
import pandas as pd

# vorwahl = pd.read_csv("200306_Vorwahl-subsetFirst20Modified.csv")
vorwahl = pd.read_csv("200306_Vorwahl-subsetFirst20Modified-Komma.csv")
intraceData = pd.read_csv("200309_DE-C3-RW-subsetFirst50Modified.csv")

# df = pd.read_csv("C:\\Users\\Public\\01_Data\\TestDataPandas\\tutorial_EdxDAT210x.csv")
# print(df)

# This is all the same way to print the first column
# print(pd.__version__)
# print(vorwahl.describe())
# print(len(vorwahl))
# vorwahl[['Ortsnetzname']]

# print(vorwahl)
print(vorwahl.dtypes)
print("-----" * 5)
print(vorwahl.info)
print("-----" * 5)
print(vorwahl.head())
print("-----" * 5)
print(vorwahl.columns)
print("-----" * 5)
print(vorwahl["Ortsnetzkennzahl"])
print("--IterRows---" * 5)
for i,j in vorwahl.iterrows():
    print(i,1)
    print()
print("--IterColumns---" * 5)
ortKennColumns = list(vorwahl)
for line in ortKennColumns:
    print(vorwahl[line][2])
print("-----" * 5)

'''
print(intraceData)
print(intraceData.columns)
print(intraceData["company_name"])

print("-----" * 5)

src_str = 'using in opertor in Python'

a_bool = 'in' in src_str
b_bool = 'out' in src_str

print("Source string")
print("The term 'in' exists?" , a_bool)
print("The term  'out' existrs?" , b_bool)

print("--- ---" * 5)


##############################
# def findVorwahl:  

# Takes a row
# Checks for vorwahl
# if yes: add okay to row
#############################


############################
# in Operator with numbers

src_str = '49 201136960'


# in operator finds a substring and returns a TRUE if found
a_bool = '201' in src_str
b_bool = 'out' in src_str

print("Source string")
print("The term '201' exists?" , a_bool)
print("The term  'out' existrs?" , b_bool)


print( vorwahl['Ortsnetzname']     )

print( df[['col0']]   )
print( vorwahl.loc[:, 'Ortsnetzname']   )
print( df.loc[:, ['col0']] )
print( df.iloc[:, 0]  )
print( df.iloc[:, [0]] )
#   print( df.ix[:, 0])     bug message: dataframe has no ix attribute

# Boolean Indexing
print("-- Bolean indexing --")
print( df.col0 < 0      )
print( df[df.col0 < 0]  )
print( df[ (df.col0<0) | (df.col1<0) ]   )

# Changing a value
df[df < 0] = -100  
print(df)
'''