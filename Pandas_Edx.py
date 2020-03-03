#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn use pandas module
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\Public\\01_Data\\TestDataPandas\\tutorial_EdxDAT210x.csv")
print(df)

# This is all the same way to print the first column
print( df.col0        )
print( df['col0']     )
print( df[['col0']]   )
print( df.loc[:, 'col0']   )
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