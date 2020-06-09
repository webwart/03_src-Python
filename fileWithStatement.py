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

import pathlib as pl


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

def write_f_inSubDir(prevLastLine  , b_line , lineBlock):
    ''' Writes the content to a file and saves it in a SubDir'''
    fileName  = (str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_WithState.csv")
    file = pl.Path.cwd().joinpath("TestSubDir" , fileName )
    with open(file, 'w') as nf:
        nf.write(lineBlock)



def read_f_all(f): 
    ''' Reads and returns the content in a list '''
    pass

def main():
    created_content = create_Lines( 5 , "this is a crazy line")
    content = ""
    for line in created_content:
        content = f'{content}\n{line}'
    print(content)
    write_f_inSubDir(1  , 5 , content)

if __name__ == "__main__":
    main()
