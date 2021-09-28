#!/user/  .in Unix only

#  ------------------------------------
#  Porject: DEV - Converting URLs
#   Author: Rainer Warth
#  Version: 27-09-2021
#    Goals: Read URLs and their description from a file. Convert int .md , .rst , json , SQL format.
#      Ref: Public\03_src\python\dictionaryJobUrl.py
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: run if /Data_Test is filled with test data
#       >N: 
#  --------------------- 

import pathlib as pl
import re
import json
from datetime import datetime , date

def read_File_In_List(subDir , fileName):
    ''' subDir = name of subDir
        fn_JobLink = name file from which the content is read into a list
        returns = list with file content '''
    filePath = pl.Path.cwd().joinpath(subDir , fileName )
    with open(filePath) as f:
        return list(f)


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

def parse_URL_ContentList( list_Content , regEx_StartLine , regEx_MidLine, regEx_EndLine):
    ''' list_Content = is a list of lines from a file 
        regEx_seperator = indicates beginning and end of a record/dictionary 
        regEx_key = indenfies the keys through begin and end signatures'''
    n_line = 0
    records_as_dictio =[]
    record_dictio = {}
    record_START = False
    last = 0
    enum_line = " "
    records =  " "


    print(f"{regEx_StartLine}(?P<UrlName>.+){regEx_MidLine}(?P<HypLink>.+){regEx_EndLine}")
    pattern = f"{regEx_StartLine}(?P<UrlName>.+){regEx_MidLine}(?P<HypLink>.+){regEx_EndLine}"
    print(f"RegEx pattern: {pattern}")
    prog = re.compile(pattern)

    url_list_complete = []

    for i , line in enumerate(list_Content): 
        n_line = n_line + 1
        p_line = f'{i}--X {line}'
        empty_line = 0
        records = records + p_line

        if prog.match(line) :
            
            print(f'Have  mutch but cannot use groups')
            groups_tuple = prog.match(line).groups()
            print(groups_tuple)

            url_list_complete = create_dictionary_for_jason( groups_tuple , url_list_complete )

        else :
            print(f'Did not findmatch in: {line}')

    return url_list_complete

'''
        if prog.match :
            # print(f'--->Found a catorgory: {list_Content[i-1]}')
            records = records + f'-->Found URLName: {prog.match.group(1)}'
            records = records + f'-->Found HypLink: {prog.match.group(2)}'
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
                records = records + f'-->KEY: {key_name} VALUE: {line}'
                record_dictio[key_name] = line



                        # print(f'enum-{i+1}')
                        # records = records + f'enum-{i+1}'
                #record[re.match(regEx_key , line).group()] = line
        
        else:
            records = records + f'-->NO MATCH\n'
    
    # print(records_as_dictio)
            
    return records , records_as_dictio 
'''

def create_dictionary_for_jason(  link_tuple , url_list ) :

    record_dic = { 
                "Name"          : "...TEMPLATE...Do not modifiy (Name of URL)",
                "URI"           : "... (https:/, file:// ",
                "Source"        : "... (Youtube, Website, Coursera, Naples-Lab/RAI, Sion-Desk/RAI etc. )", 
                "Catagory"      : ["... (Education, Music-History, Music-Video, Company, etc. )", "etc"],
                "Summary"       : "...short free text...",
                "Dates"         : {"First_entry":"2021-09-25", "Last_visit":"yyyy-mm-dd" , "Check" : True },
                "Active"        : True ,
                "Journal"       : {"SAT 25-09-2021":"Created this record...(use >N: and FUP)", "MON 11-11-1111" : "This is an older entry ...(Events like upgrade change of price, or thoughts, planning)"}
                }

    record_dic["Name"] = link_tuple[0]
    record_dic["URI"] = link_tuple[1]

    url_list.append(record_dic)

    return url_list 



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

def main():

    subDir = "Data_Test"
    fn_rst_favoritenURL = "FavoritenURLs-Part1.rst"
    # fn_RefDictio = "RefDictioJoblin.rst"
    # fn_CorDictio = "200611_Joblink-NEW.rst"
    fn_json_favoritenURL = fn_timestemp( "o" , "URLs-RKW-New" , ".json")
    # * `Österreichisches Bundesministerium für Digitalisierung und Wirtschaftsstandort, BMDW <https://termino.gv.at>`_   
    regEx_StartRstHyp = "\* `"
    regEx_MidRstHyp = "<"
    regEx_EndRstHyp = ">`_"

    list_Content = read_File_In_List(subDir , fn_rst_favoritenURL)
    print("***Read list_Content***" * 3 )
    print(list_Content)
    print("***End  list_Content***" * 3)
    print("--- --- --- " * 3)

    name_url_dictio = parse_URL_ContentList( list_Content , regEx_StartRstHyp , regEx_MidRstHyp, regEx_EndRstHyp)

    print("***Start - Name Url Dcitio***" * 3 )
    print(name_url_dictio)
    print("***End - Name Url Dcitio***" * 3 )

    write_jsonFile_CorrectedDictios(subDir , fn_json_favoritenURL , name_url_dictio )
    



    '''
    records_write_file , list_w_corrected_dictios = parse_Dictio_From_ContentList( list_Content , regEx_seperator , regEx_key , regEx_RecEnd)
    print(write_file_CorrectedDictios(subDir , fn_CorDictio , records_write_file) )

    print(list_w_corrected_dictios)

    with open("02_dumpListCorrectedDictios.json", "w") as write_file:
        json.dump(list_w_corrected_dictios, write_file, indent=4)
    '''

#    list_w_Dictios = read_records_from_file(subDir , filename_JobLink)
#    list_w_corrected_dictios = compareToRefDictio ( list_w_Dictios , filename_RefDictio)
#    outcome_message = write_file_CorrectedDictios(filename_CorDictio , list_w_corrected_dictios )
#   print(outcome_message)

if __name__ == "__main__":
    main()