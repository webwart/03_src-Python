#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 09-06-2020
#    Goals: Learn dealing with files using the "with" statement
#      Ref: https://jeffknupp.com/blog/2016/03/07/improve-your-python-the-with-statement-and-context-managers/
#      Ref: https://docs.python.org/3/tutorial/inputoutput.html   
# Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------

import pathlib as Path


f = 'some path'

def create_Lines(number_of_lines , text_in_line):
    ''' Creates a tuple with strings representing lines '''
    content = []
    n = 0
    while n < number_of_lines:
        n = n + 1
        line = f'-{n}- {text_in_line}'
        content.append(line)
    return content

def write_f_all(f):
    ''' Writes the content to a file '''
    pass

def read_f_all(f): 
    ''' Reads and returns the content in a list '''
    pass

def main():
    created_content = create_Lines( 5 , "this is a crazy line")
    print(created_content)

if __name__ == "__main__":
    main()
