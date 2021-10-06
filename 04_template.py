# -*- coding: utf-8 -*-

#  ------------------------------------
#  Porject: LEARN - template to read files and save file in the Data_Test or Data_Real directory. 
#         : The files names can be defined with the fn_timestamp function, which takes io-tag, filename, file-extension
#   Author: Rainer Warth
#  Version: 06-10-2021 Previous: -- First: --
#    Goals: Create a very generic template for reading and saving files to the data directory.
#      Ref: https://realpython.com/documenting-python-code/
#      Ref: https://realpython.com/lessons/type-hinting/
#      Ref: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc
#    Satus: runs - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs (use VScode Outline to refactor)
#   DevOps: Installed python 3.10 on Naples-Lap. I can use python for 3.9 and py for 3.10. Github repo. FSY vio github.
#   Tested: Win10 Python 3.9
#       >N: Refactor functions remove not needed functions, introduce type hints

import pathlib as pl
import re
import json
from datetime import datetime , date
import copy

# example for type hingint

def read_File_In_List(subDir: str , fileName: str) -> list :
    """Gets and prints the spreadsheet's header columns (numpy format)

    Parameters
    ----------
    subDir : str
        Directory location
    fileName : str
        Filename, often created by def file_timestamp

    Returns
    -------
    list
        The elements are the lines of the file at location subDir/filename
    """
    
    filePath = pl.Path.cwd().joinpath(subDir , fileName )
    with open(filePath) as f:
        return list(f)

def load_dictio_from_rstFile (file_Obj):
    ''' Return: Dictionary all other dictionaries are compared to '''
    return ref_dictio

def parse_Dictio_From_ContentList( list_Content , regEx_seperator , regEx_key, regEx_RecEnd):
    ''' list_Content = is a list of lines from a file 
        regEx_seperator = indicates beginning and end of a record/dictionary 
        regEx_key = indenfies the keys through begin and end signatures
        NOTE:        Records are only transfered to the dictionary list if a catagory is recognized !!
        >N: add catagory to the key:vaue catagory        '''
    n_line = 0
    records_as_dictio =[]
    record_dictio = {}
    record_START = False
    last = 0
    enum_line = " "
    records =  " "
    for i , line in enumerate(list_Content): 
        n_line = n_line + 1
        p_line = f'{i}--X {line}'
        empty_line = 0
        print(p_line)
        records = records + p_line
        
        if re.match(regEx_seperator, line) and re.match(regEx_seperator , list_Content[i+2]):
            # print(f'--->Found a catorgory: {list_Content[i-1]}')
            catagory_value = list_Content[i+1]
            # records = records + f'-->Found Catorgory: {catagory_value}'
            records = records + f'-->Found Catorgory: {list_Content[i+1]}'
            last = n_line
            
                # records = records + f'#{n_line}#{line}'
                # records = records + f'enum-{i+1}'
            lineControl = True

        elif re.match(regEx_seperator, line) and re.match(regEx_key , list_Content[i+2]):
            records = records + f'-->Found Record start:\n' 
            record_START = True

        elif re.match(regEx_key , line) and record_START:
            if re.match(regEx_RecEnd , line ):
                records = records + f'-->Found: Record end:\n'
                record_START = False
                records_as_dictio.append(record_dictio)
                record_dictio = {}
            else:
                key_name = re.match(regEx_key , line).group()
                if key_name == "Catagory":
                    records = records + f'-->KEY: {key_name} VALUE: {catagory_value}'
                    record_dictio[key_name] = catagory_value
                records = records + f'-->KEY: {key_name} VALUE: {line}'
                record_dictio[key_name] = line

                        # print(f'enum-{i+1}')
                        # records = records + f'enum-{i+1}'
                #record[re.match(regEx_key , line).group()] = line
        
        else:
            records = records + f'-->NO MATCH\n'
    
    # print(records_as_dictio)
            
    return records , records_as_dictio 

def write_file_CorrectedDictios(subDir , filename_CorDictio , list_w_corrected_dictios ):
    ''' param filename_CorDictio = list with corrected dictios
        param list_w_corrected_dictios = filenme to which the list content is writen.
        does = writes a fle 
        return = String with info about writen content  

        def  saveContentInNewFile(lineTuple, lineBlock):
        breaklistTuple is the tuple from breakList, lineBlock is string with lines  '''
    
    # prevLastLine , b_line = lineTuple
    
    # print(str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")
    # fileName  = (str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")
    fn = filename_CorDictio
    file = pl.Path.cwd().joinpath(subDir , fn )
    with open(file, 'w') as nf:
        nf.write(list_w_corrected_dictios)

    return f"I wrote the above content to {filename_CorDictio}"

def write_jsonFile_CorrectedDictios(subDir , filename_CorDictio , list_w_corrected_dictios ):
    ''' param filename_CorDictio = list with corrected dictios
        param list_w_corrected_dictios = filenme to which the list content is writen.
        does = writes a fle 
        return = String with info about writen content  

        def  saveContentInNewFile(lineTuple, lineBlock):
        breaklistTuple is the tuple from breakList, lineBlock is string with lines  '''
    
    # prevLastLine , b_line = lineTuple
    
    # print(str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")
    # fileName  = (str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")
    fn = filename_CorDictio
    file = pl.Path.cwd().joinpath(subDir , fn )

    with open(file , "w") as nf:
        json.dump(list_w_corrected_dictios, nf, indent=4)
    
    return f"I wrote the above content to {filename_CorDictio}"

def fn_timestemp( io_tag: str , part_1: str , extension: str) -> str:
    """[summary]
    return: string , to be used as filename
    import: from datetime import datetime
    part_1:  <yymmdd>_<part_1>_<source>.<ext>
    extension:  extension of the filename. e.g.  .rst , .txt , .md
    The function creates a timestemp string.
    :return: [description]
    :rtype: str
    """        
    now = datetime.now()
    fn_timestemp = now.strftime("%y%m%d-%H%M")
    fn_center = part_1
    fn_ext = extension
    fn_io = io_tag
    return (f'{fn_io}-{fn_timestemp}_{fn_center}{fn_ext}')

def show_content_listDictio (listDictio_obj , listDictioName_obj):
    print(f'-- Inside def show_content_listDictio showing --> {listDictioName_obj}')
    for dictio in listDictio_obj:
        print(f'\t{dictio}' )
    print(f'-- End of def show_content_listDictio showing --> {listDictioName_obj} \n')

def make_new_dictio (ref_dir_Obj , old_dir_list_Obj):
    ''' compare old_dictio to ref_dir and create new_dir  '''
    new_dictio_list = []
    n = 0
    for dictio in old_dir_list_Obj:
        n = n + 1
        print(f'\nin def m_n_d--dictio {dictio} ----- { n } ')
        ref_dir_Copy = copy.deepcopy(ref_dir_Obj)   # new dictio obj
        print(f'in def m_n_d--ref_dir_Copy after deepcopy {ref_dir_Copy}')
        ref_dir_Copy.update(dictio)
        print(f'in def m_n_d--ref_dir_Copy after update: {ref_dir_Copy}')
        
        new_dictio_list.append(ref_dir_Copy)
        print(f'in def m_n_d--new_dictio_list : {new_dictio_list}')

    print(f"\n --- return new_dictio_list" * 5)
    print(f'\n before def m_n_d--new_dictio_list ((3)) {new_dictio_list}')
    print(f"\n ---" * 5)
    return new_dictio_list

def main():

    ## Switch to real data
    '''
    dn_Data = r"./Data_Real"
    fn_rstFile_JobLink = r"n-200607_JobLinks.rst"
    '''
    
    ## Switch to Test 
    dn_Data = r"./Data_Test"
    fn_rstFile_JobLink = r"i-TEST-joblink.rst"
    
    fn_rstFile_RefDictio = r"i-RefDictioJoblink.rst"
        
    fn_dictios_Ref = fn_timestemp( "o" , "Records-Dictio-Ref" , ".rst")
    fn_dictios_JobLink = fn_timestemp( "o" , "Records-Dictio-JobLink" , ".rst")
    fn_dictioJson_Ref = fn_timestemp( "o" , "dictio_Ref" , ".json")
    fn_dictioJson_JobLink = fn_timestemp( "o" , "dictio_JobLink" , ".json")
    fn_dictioJson_JobLinkCorrect = fn_timestemp( "o" , "dictio_JobLinkCorrect" , ".json")
    
    # regEx_RecStart = "-------------------------------------------------------------------------------"
    regEx_seperator = "-------+"
    regEx_key = ":.*?:"
    regEx_RecEnd = ":end:"

    print(" ----- Start list_fileContent\n" * 3)
    list_fileContent = read_File_In_List(dn_Data , fn_rstFile_RefDictio)
    list_fileContent_JobLink = read_File_In_List(dn_Data , fn_rstFile_JobLink)
    print(list_fileContent)

    print(" ----- Start list_fileContent_JobLink\n" * 3)
    print(list_fileContent_JobLink)

    print(" ----- Start parse_Dictio_From_ContentList" * 5)
    records_write_file , list_w_corrected_dictios = parse_Dictio_From_ContentList( list_fileContent , regEx_seperator , regEx_key , regEx_RecEnd)
    records_write_file_JobLink , list_w_corrected_dictios_JobLink = parse_Dictio_From_ContentList( list_fileContent_JobLink , regEx_seperator , regEx_key , regEx_RecEnd)

    write_file_CorrectedDictios(dn_Data , fn_dictios_Ref , records_write_file)  # ref
    write_file_CorrectedDictios(dn_Data , fn_dictios_JobLink , records_write_file_JobLink)   # joblink 

    print(" ----- print(list_with_corrected_dictios\n" * 5)
    print(list_w_corrected_dictios)
    print(" ----- print(list_with_corrected_dictios_JobLink\n" * 5)
    print(list_w_corrected_dictios_JobLink)

    write_jsonFile_CorrectedDictios(dn_Data , fn_dictioJson_Ref , list_w_corrected_dictios )
    write_jsonFile_CorrectedDictios(dn_Data , fn_dictioJson_JobLink , list_w_corrected_dictios_JobLink )
    
    #  Correct of dictios
    print(f" ----- Show dictio from list -------:{list_w_corrected_dictios[0]}" )
    list_correctDictios_Joblinks = make_new_dictio( list_w_corrected_dictios[0] , list_w_corrected_dictios_JobLink)

    write_jsonFile_CorrectedDictios(dn_Data , fn_dictioJson_JobLinkCorrect , list_correctDictios_Joblinks )

                    