#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 08-08-2020
#    Goals: Compare dictionaries to a reference. Use of deepcopy
#      Ref: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#      Ref: https://realpython.com/python-dicts/#dupdateobj
#   Ref_By: /07_Jobworksapce/dictionaryComparyRefDir
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: 
#       >N: --
#  ---------------------  

from datetime import date, time, datetime
import copy

ref_dictio = {"name": "(ref_name)", "age": "(ref_age , some number)", "url": "(ref_url, some url)"} 
old_dictio = {"name" : "old_name" , "age" : "old_age"}

old_dictio_list = [ 
                {"name": "(ref_name)", "age": "(ref_age , some number)", "url": "(ref_url, some url)"} ,
                {"name" : "old_name_2" , "age" : "old_age_2" , "url": "old_url_2"} ,
                {"name" : "old_name_2" , "age" : "old_age_2"} , 
                {"name" : "old_name_1" , "age" : "old_age_1" , "url" : "https://xnxx_1.com"} , 
                {"name" : "old_name_3" , "age" : "old_age_3" , "another_key"  : "love string_4"} ,
                {"name" : "old_name_4" , "age" : "old_age_4" , "url" : "https://google_4.com" , "another_key"  : "love string_5"} ,
                ]


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

def show_content_listDictio (listDictio_obj , listDictioName_obj):
    print(f'-- Inside def show_content_listDictio showing --> {listDictioName_obj}')
    for dictio in listDictio_obj:
        print(f'\t{dictio}' )
    print(f'-- End of def show_content_listDictio showing --> {listDictioName_obj} \n')

def main():
    print("¦¦------------------")
    today = date.today()
    print(f'¦¦ {today} ')
    print("¦¦------------------")
    
    print("\n ----- Variables ----- \n" )

    print(f"ref_dir reciev  : {ref_dictio}")
    print(f"old_dir source  : {old_dictio}")   
    show_content_listDictio(old_dictio_list , "old_dictio_list")

    new_dictio_list = make_new_dictio(ref_dictio , old_dictio_list)
   
    print(f"ref_dir updated : {ref_dictio}")
    show_content_listDictio(new_dictio_list , "new_dictio_list")


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