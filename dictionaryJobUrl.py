#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 11-06-2020
#    Goals: Learn to read records from a file into dictionary. Compare dictionary to a reference.
#      Ref: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#      Ref: https://docs.python.org/3.7/howto/regex.html
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------ 

import pathlib as pl
import re



def read_File_In_List(subDir , fileName):
    ''' subDir = name of subDir
        fn_JobLink = name file from which the content is read into a list
        returns = list with file content '''
    filePath = pl.Path.cwd().joinpath(subDir , fileName )
    with open(filePath) as f:
        return list(f)
    pass

def parse_Dictio_From_ContentList( list_Content , regEx_seperator , regEx_key):
    ''' list_Content = is a list of lines from a file 
        regEx_seperator = indicates beginning and end of a record/dictionary 
        regEx_key = indenfies the keys through begin and end signatures'''
    n_line = 0
    record = {}
    lineControl = True
    last = 0
    for i , line in enumerate(list_Content): 
        n_line = n_line + 1
        record['linNum'] = n_line
        empty_line = 0

        if re.match(regEx_seperator, line):
            if n_line - last == 2 :
                print(f'--->Found a catorgory: {list_Content[i-1]}')
            last = n_line
            print(f'#{n_line}#{line}')
            print(f'enum-{i+1}')
            lineControl = True
        elif re.match(regEx_key , line) and lineControl :
            print(f'#{n_line}>>KEY>> {line}')
            print(f'enum-{i+1}')
            record[re.match(regEx_key , line).group()] = line
        else:
            print(f'{n_line}# # # #')
            print(f'enum-{i+1}')
            empty_line = empty_line + 1
            if empty_line == 2:
                lineControl = False
            print("//// record /////")
            print(record)
            


def compareToRefDictio ( list_w_Dictios , lists_w_RefDictio):
    ''' compare list with with dictionaries with a ref directory. 
        A new dictionary like the ref dictionary is created with the content of the dictionary from the list. 
        All new dictionaries are stored in a list.
        returns = list '''
    pass

def write_file_CorrectedDictios(filename_CorDictio , list_w_corrected_dictios ):
    ''' param filename_CorDictio = list with corrected dictios
        param list_w_corrected_dictios = filenme to which the list content is writen.
        does = writes a fle 
        return = String with info about writen content  '''
    pass


def main():

    subDir = "TestSubDir"
    fn_JobLink = "joblink.rst"
    fn_RefDictio = "RefDictioJoblin.rst"
    fn_CorDictio = "200611_Joblink-NEW.rst"

    regEx_seperator = "-----------+"
    regEx_key = ":.+:"

    list_Content = read_File_In_List(subDir , fn_JobLink)
    print("**Read list_Content****" * 20)
    print(read_File_In_List(subDir , fn_RefDictio))
    print("******" * 20)
    parse_Dictio_From_ContentList( list_Content , regEx_seperator , regEx_key)

#    list_w_Dictios = read_records_from_file(subDir , filename_JobLink)
#    list_w_corrected_dictios = compareToRefDictio ( list_w_Dictios , filename_RefDictio)
#    outcome_message = write_file_CorrectedDictios(filename_CorDictio , list_w_corrected_dictios )
#   print(outcome_message)

if __name__ == "__main__":
    main()
