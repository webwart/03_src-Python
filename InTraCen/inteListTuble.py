import random



inteList = []

def inteListTubel( startLine , endLine , minRand , maxRand ):
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


print(inteListTubel(599 , 5766 , 40 , 42 ))