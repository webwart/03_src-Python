 #!/user/  .in Unix only
# -*- coding: utf-8 -*-

#  ------------------------------------
#  Porject: LEARN - template
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: -- First: --
#    Goals: Learn Urllib
#      Ref: 
#      Ref:  
#      Ref: 
#    Satus: runs - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: bub
#       >N: --

import pathlib as pl
import re
import json
from datetime import datetime , date
import copy

def read_File_In_List(subDir , fileName):
    ''' subDir = name of subDir
        fn_JobLink = name file from which the content is read into a list
        returns = list with file content '''
    filePath = pl.Path.cwd().joinpath(subDir , fileName )
    with open(filePath) as f:
        return list(f)

def fn_timestemp( io_tag , part_1 , extension):
    ''' return: string , to be used as filename
        import: from datetime import datetime
        part_1:  <yymmdd>_<part_1>_<source>.<ext>
        extension:  extension of the filename. e.g.  .rst , .txt , .md
        The function creates a timestemp string.
    '''
    now = datetime.now()
    fn_timestemp = now.strftime("%y%m%d-%H%M")
    fn_center = part_1
    fn_ext = extension
    fn_io = io_tag
    return (f'{fn_io}-{fn_timestemp}_{fn_center}{fn_ext}')


def main():   
    ## Switch to real data
    '''
    dn_Data_Real = r"./Data_Real"

    fn_rstFile_JobLink = r"n-200607_JobLinks.rst"
    '''
    
    ## Switch to Test
    dn_Data_Test = r"./Data_Test"
    
    fn_rstFile_JobLink = r"i-TEST-joblink.rst"
    
    fn_rstFile_RefDictio = r"i-RefDictioJoblink.rst"
        
    fn_dictios_Ref = fn_timestemp( "o" , "Records-Dictio-Ref" , ".rst")
    fn_dictios_JobLink = fn_timestemp( "o" , "Records-Dictio-JobLink" , ".rst")
    fn_dictioJson_Ref = fn_timestemp( "o" , "dictio_Ref" , ".json")
    fn_dictioJson_JobLink = fn_timestemp( "o" , "dictio_JobLink" , ".json")
    fn_dictioJson_JobLinkCorrect = fn_timestemp( "o" , "dictio_JobLinkCorrect" , ".json")
    
    regEx_seperator = "-------+"


if __name__ == "__main__":
    main()