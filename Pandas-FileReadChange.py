# LEARN: read, change, append, create new file
# Reference: ipython cookbook, chapter 1- Reading from a CSV
# Date: 21.01.2016

import pandas as pd
print ("Pandas is ready")

# print(open("C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\Python\\TestDataPandas\\bikes.csv").read())
print(open(".\\TestDataPandas\\bikes.csv").read())
print ("----------------------------------------------- use pd.read_CSV from pandas")
broken_df = pd.read_csv('.\\TestDataPandas\\bikes.csv')
# broken_df = pd.read_csv("C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\Python\\TestDataPandas\\bikes.csv")
# broken_df[:3]

