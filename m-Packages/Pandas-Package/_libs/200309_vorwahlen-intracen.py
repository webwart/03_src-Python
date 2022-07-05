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
import sqlite3 as sq
import re


def main():

    # vorwahl = pd.read_csv("200306_Vorwahl-subsetFirst20Modified.csv" , sep=";")
    # vorwahl = pd.read_csv("200306_Vorwahl-subsetFirst20Modified-Komma.csv")
    # intraceData = pd.read_csv("200309_DE-C3-RW-subsetFirst50Modified.csv" , sep=";" )

    intraceData = pd.read_csv(".\\I200318_DE-C3-RW-copy.csv" , sep=';' )

    # df = pd.read_csv("C:\\Users\\Public\\01_Data\\TestDataPandas\\tutorial_EdxDAT210x.csv")
    # print(df)

    # This is all the same way to print the first column
    # print(pd.__version__)
    # print(vorwahl.describe())
    # print(len(vorwahl))
    # vorwahl[['Ortsnetzname']]

    '''
    print("-----" * 5 + " dtypes")
    print(vorwahl.dtypes)
    print("-----" * 5 + " info ")
    print(vorwahl.info)
    print("-----" * 5 + " head ")
    print(vorwahl.head())
    print("-----" * 5 + " columns")
    print(vorwahl.columns)
    print("-----" * 5 + "Ortsnetzkennzahl")
    print(vorwahl["Ortsnetzkennzahl"])
    print("-----" * 5 + "Print list from Ortsnetzkennzahl")
    print(list(vorwahl["Ortsnetzkennzahl"]))
    print("-----" * 5 + " list ")
    ortKennColumns = list(vorwahl)
    print(ortKennColumns)
    print("--PrintLine---" * 5)
    for line in ortKennColumns:
        print(vorwahl[line][2])
    print("-----" * 5)
    print(type(ortKennColumns))
    print("-----" * 5 + "Intracen eMail")


                                            print(intraceData.head())
                                        print("-----" * 5 + "list eMail")

    '''
    print(intraceData.columns)
    eMailList = list(intraceData["email_1                            "])
    print("-----" * 5 + "Length eMail list intracen")
    counter = 0
    mRegEx = '.*@.*'
    noEmail = 0
    yesEmail = 0

    for x in eMailList:
        matchForRegEx = re.search(mRegEx , x)  
        if matchForRegEx == None: 
            noEmail = noEmail + 1
        else:
            yesEmail = yesEmail + 1
        counter = counter + 1 

    print(counter)
    print(noEmail)
    print(yesEmail)
    #print("Total: {counter} noEmail: {noEmail} yesEmail: {yesEmail}".format(counter , noEmail , yesEmail  )



    ''' 
    for i,j in vorwahl.iterrows():
        print(i,1)
        print()

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



if __name__ == "__main__":
    main()