# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\Public\\Documents\\Pub_CodeDev\\Python\\TestDataPandas\\tutorial_EdxDAT210x.csv")
print(df)

# This is all the same way to print the first column
print( df.col0        )
print( df['col0']     )
print( df[['col0']]   )
print( df.loc[:, 'col0']   )
print( df.loc[:, ['col0']] )
print( df.iloc[:, 0]  )
print( df.iloc[:, [0]] )
print( df.ix[:, 0])

# Boolean Indexing
print("-- Bolean indexing --")
print( df.col0 < 0      )
print( df[df.col0 < 0]  )
print( df[ (df.col0<0) | (df.col1<0) ]   )

# Changing a value
df[df < 0] = -100  
print(df)