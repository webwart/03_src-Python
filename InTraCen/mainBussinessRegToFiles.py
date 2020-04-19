import random
import pathlib

# TEST-FILE= 0001-0001_BusinessRegister-MultiEmail.csv


def inteListTubel( startLine , endLine , minRand , maxRand , inteList ):
    ''' return list with tuples containing two intergeers '''
    r_num = random.randrange( minRand , maxRand)
    while (endLine - maxRand ) > startLine :
        if startLine == 0 :
            pos1 = 0
            pos2 = r_num    # lets say 45
            startLine = pos2 + 1
            inteList.append((pos1 , pos2))
        else :
            pos1 = startLine
            pos2 = startLine + r_num    # lets say 45
            startLine = pos2 + 1
            inteList.append((pos1 , pos2))
    pos1 = startLine
    pos2 = endLine
    inteList.append((pos1 , pos2))

    return inteList

def readFileInList(fileName):
    ''' return a list all lines in the input file '''
    with open(fileName) as f:
        return list(f)

def getLinesFromFile( lineTuple , allLineList):
    '''/ lineList contains all lines from a file, 
         lineTuple contains the start and end line of block of lines
         return =  string with  '''

    contentBlock = ""
    firstLine_Block , lastLine_Block = lineTuple
    print(str(firstLine_Block) + "--blockTEST--" + str(lastLine_Block))
    
    for counter, value in enumerate(allLineList):
        if ((counter >= firstLine_Block) and ( counter <= lastLine_Block )):
            print(value, end= "")
            contentBlock = contentBlock + value
    return contentBlock


def  saveContentInNewFile(lineTuple, lineBlock):
    ''' breaklistTuple is the tuple from breakList, lineBlock is string with lines  '''
    prevLastLine , b_line = lineTuple
    print(str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")
    fileName  = (str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")
    file = pathlib.Path.cwd().joinpath("InTraCenTestFiles" , fileName )
    with open(file, 'w') as nf:
        nf.write(lineBlock)


def main():
    inteList = []
    print(inteListTubel(599 , 5766 , 80 , 120 , inteList))

    print("-----readFileInList-----" * 5)
    lineListB = readFileInList("n-200403_eMailBusinessRegister_RKW.csv")
    print("-----getLinesFromFile-----" * 5)
    # lineBlock = getLinesFromFile((0 , 20), lineListB)
    # print(lineBlock)
    for block in inteList:
        lineBlock = getLinesFromFile(block, lineListB )
        saveContentInNewFile(block, lineBlock )

if __name__ == "__main__":
    main()