import random
import pathlib

# TEST-FILE= 0001-0001_BusinessRegister-MultiEmail.csv

def getLinesFromFile( lineTuple , lineList):
    ''' lineList contains all lines from a file, lineTuple contains the start and end line of block of lines '''
    firstLine_Block , lastLine_Block = lineTuple
    print(str(firstLine_Block) + "--blockTEST--" + str(lastLine_Block))

def readFileInList(fileName):
    ''' return a list all lines in the input file '''
    with open(fileName) as f:
        return list(f)

def  saveContentInNewFile(breakList):
    for  prevLastLine , b_line in breakList:
        print(str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")
        fileName  = (str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")
        file = pathlib.Path.cwd().joinpath("InTraCenTestFiles" , fileName )
        with open(file, 'w') as nf:
            nf.write("content in" + fileName )


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

def main():
    inteList = []
    print(inteListTubel(599 , 5766 , 400 , 500 , inteList))
    print("-----saveContentInNewFile-----" * 5)
    # print(saveContentInNewFile(inteList))
    
    lineList = []
    lineListB = readFileInList("0001-0001_BusinessRegister-MultiEmail.csv")
    for block in inteList:
        getLinesFromFile(block, lineList )
    
    print("-----readFileInList-----" * 5)
    print(lineListB)


if __name__ == "__main__":
    main()