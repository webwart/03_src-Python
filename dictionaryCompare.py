#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 08-08-2020
#    Goals: Compare dictionaries to a reference.
#      Ref: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#      Ref: https://docs.python.org/3.7/howto/regex.html
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: 
#       >N: Develop way to compare to template dictionary. Load a dictionary from a reference file or .rst file.
#  --------------------- 

ref_dir = {"name" : "ref_name" , "age" : "ref_age"} 
old_dir = {"name" : "old_name" , "age" : "old_age"}
old_dir_list = [ {"name" : "old_name_1" , "age" : "old_age_1"} , {"name" : "old_name_2" , "age" : "old_age_2"} , {"name" : "old_name_3" , "age" : "old_age_3"}]
new_dir_list = []

new_dir = ref_dir.update(old_dir)

fn_rstFile = r"./TestSubDir/RefDictioJoblink.rst"

def load_dictio_from_rstFile (file_Obj):
    ''' Return: Dictionary all other dictionaries are compared to '''
    return ref_dictio

def make_new_dir (dictio_Obj):
    ''' compare old_dictio to ref_dir and create new_dir
    if old_dictio and ref_dir have same keys:
        make new_dir
    else: 
        print(old_dictio[name])    '''
    return new_dir 

print(old_dir_list)

