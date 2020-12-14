#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN - Creatiofile of files and directories with pathlib
#   Author: Rainer Warth
#  Version: 05-12-2020
#    Goals: Use pathlib to create files/directories and work with them.
#      Ref: https://www.youtube.com/watch?v=YwhOUyTxXVE -> PyCharm tutorial serious What does this package
#      Ref: https://docs.python.org/3/library/pathlib.html -> py doc
#      Ref: https://docs.python.org/3/library/exceptions.html?highlight=ioerror#IOError -> py doc
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------

"""
Description:  
 
Test_Data file:
"""

from pathlib import Path
import shutil    # only needed if I want to delet the Test file/directory

''' --SART-- Use these lines to delete directory  
    --END--  use these lines to delete directory '''

try:
    shutil.rmtree('Test_Data_Output\\')
except IOError:
    print("Directory/file does not excist ")

''' >N: Use the code below to create a rmtree function s in shutil
    new_file_path2.unlink()
    new_file_path.rmdir() '''



def main():
    new_path = Path('.')
    new_file_path = new_path / 'Data_Test_Output'
    new_file_path2 = new_file_path / 'o-pathlib_stuff2.txt'
    print(new_file_path)
    print(new_file_path2)
    print("-" * 10)
    print(new_file_path.resolve())
    print(new_file_path2.resolve())
    print(type(new_file_path))
    
    print("--S--" + "making directory" + "-" * 5)
    new_file_path.mkdir()
    print(new_file_path.exists())
    new_file_path2.touch()    # touch() does not create a directory for you

    
    print(new_file_path2.exists())
    print(f'Is it a directory: {new_file_path.is_dir}')


if __name__ == "__main__":
    main()