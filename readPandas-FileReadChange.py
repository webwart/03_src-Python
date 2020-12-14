#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn use pandas module. read, change, append, create new file
#      Ref: ipython cookbook, chapter 1- Reading from a CSV
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------

import pandas as pd
print ("Pandas is ready")

# print(open("C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\Python\\TestDataPandas\\bikes.csv").read())
print(open(".\\TestDataPandas\\bikes.csv").read())
print ("----------------------------------------------- use pd.read_CSV from pandas")
broken_df = pd.read_csv('.\\TestDataPandas\\bikes.csv')
# broken_df = pd.read_csv("C:\\Users\\rwarth\\PUB-Documents\\Pub_CodeDev\\Python\\TestDataPandas\\bikes.csv")
# broken_df[:3]

