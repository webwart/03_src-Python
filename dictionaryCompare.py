#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 08-08-2020
#    Goals: Compare dictionaries to a reference.
#      Ref: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#      Ref: https://realpython.com/python-dicts/#dupdateobj
#   Ref_By: /07_Jobworksapce/dictionaryComparyRefDir
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: 
#       >N: Develop way to compare to template dictionary. Load a dictionary from a reference file or .rst file.
#  ---------------------  


old_dir_list = [ {"name" : "old_name_1" , "age" : "old_age_1" , "url" : "https://xnxx_1.com"} , 
                {"name" : "old_name_2" , "age" : "old_age_2"} , 
                {"name" : "old_name_3" , "age" : "old_age_3" , "another_key"  : "love string_4"} ,
                {"name" : "old_name_4" , "age" : "old_age_4" , "url" : "https://google_4.com" , "another_key"  : "love string_5"} ,
                ]
new_dir_list = []




def make_new_dir (ref_dir_Obj , old_dir_list):
    ''' compare old_dictio to ref_dir and create new_dir  '''
    for dir in old_dir_list:
        ref_dir.update(dir)
        new_dir_list.append(ref_dir)
        ref_dir.clear()
    
    return new_dir_list


def main():
    ref_dir = {"name": "(ref_name)", "age": "(ref_age , some number)", "url": "(ref_url, some url)"} 
    print(f"ref_dir before update: {ref_dir}")
    old_dir = {"name" : "old_name" , "age" : "old_age"}
    print(f"old_dir before update: {old_dir}")

    ref_dir = ref_dir.update(old_dir)

    print(f"ref_dir updated: {ref_dir}")
    print(f"old_dir updated: {old_dir}")


    d1 = {'a': 10, 'b': 20, 'c': 30}
    print(f"d1 before update: {d1}")
    d2 = {'b': 200, 'd': 400, 'name' : 'old_name'  }
    print(f"d2 before update: {d2}")
    
    d1.update(d2)
    
    print(f"d3 updated: {d1}")     #expected {'a': 10, 'b': 200, 'c': 30, 'd': 400}
    print(f"d2 updated: {d2}")
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
    '''


if __name__ == "__main__":
    main()