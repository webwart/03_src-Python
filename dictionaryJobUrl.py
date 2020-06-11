#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 11-06-2020
#    Goals: Learn to read records from a file into dictionary. Compare dictionary to a reference.
#      Ref: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------ 

import pathlib as pl

def read_records_from_file(subDir , filename_JobLink):
    ''' read file with jobLink records into a list with dictionaries
        returns = list '''
    pass



def compareToRefDictio ( list_w_Dictios , filename_RefDictio):
    ''' compare list with with dictionaries with a ref directory. If different a new dictionary like the ref dictionary is created
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
    filename_JobLink = "Joblink.rst"
    filename_RefDictio = "RefDictioJoblin.rst"
    filename_CorDictio = "200611_Joblink-NEW.rst"

    list_w_Dictios = read_records_from_file(subDir , filename_JobLink)
    list_w_corrected_dictios = compareToRefDictio ( list_w_Dictios , filename_RefDictio)
    outcome_message = write_file_CorrectedDictios(filename_CorDictio , list_w_corrected_dictios )
    print(outcome_message)



if __name__ == "__main__":
    pass

