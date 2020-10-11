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

def make_new_dir (ref_dir_Obj , old_dir_list):
    ''' compare old_dictio to ref_dir and create new_dir
    for dir in old_dir_list:
        ref_dir.update(dir)
        new_dir_list.append(ref_dir)
        ref_dir.clear()
    
    return new_dir_list 
   '''


ref_dir_cp = dict(ref_dir.items())
print(type(ref_dir))
print(type(ref_dir_cp))

# Comparing Object
# https://realpython.com/python-is-identity-vs-equality/
# == compares the attributes of the object
# 'is'  checks whether two variables point to the same object in memory
print(ref_dir == ref_dir_cp)
print(ref_dir is ref_dir_cp)
