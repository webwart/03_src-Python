import random


def  saveContentInNewFile(breakList):
    for  prevLastLine , b_line in breakList:
        print(str(prevLastLine).zfill(4) + "-" + str(b_line).zfill(4) + "_BusinessRegister-Email.csv")

    '''
    lastLine = b_line
    print(str(prevLastLine) + "-"+ str(lastLine))
    prevLastLine = b_line + 1
    fileName  = (str(prevLastLine).zfill(4) + "-" + str(lastLine).zfill(4) + "_BusinessRegister-Email.csv")
    file = pathlib.Path.cwd().joinpath("InTraCenTestFiles" , fileName )
    with open(file, 'w') as nf:
        nf.write(contentToWrite)
    '''


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
    print(inteListTubel(599 , 5766 , 40 , 42 , inteList))
    print("-----" * 5)
    print(inteList)

if __name__ == "__main__":
    main()