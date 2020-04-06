
# https://realpython.com/working-with-files-in-python/
#  5766 Lines
# I will use a test file with 1000 lines.
# I  will create files with lines of 70 +- 20

import pathlib

lastLineOfFile = 8
prevLastLine = 1
lastLine = 2
contentToWrite = ""
breakList = []

for breakline in  range(5766 // 50 ):
    # print(breakline)
    multiBreakline = breakline * 50
    breakList.append(multiBreakline)

print("<--->" )
print(breakList)
print("---->" )
print(pathlib.Path.cwd())
print(pathlib.Path(r'c:\Users\Public\03_src\python\InTraCenTestFiles'))
print(pathlib.Path.home() / "InTraCenTestFiles" )           # same as with joinpath
print(pathlib.Path.home().joinpath("InTraCenTestFiles"))    # same as with / operator

pathlib.Path.cwd().joinpath("InTraCenTestFiles" , )


with open('0001-0008_BusinessRegister-Email-Test.csv', ) as f:
    for line in f:
        contentToWrite = (contentToWrite + line )
        print(str(lastLine) + "---->" + line)
        lastLine = lastLine + 1
        # f.w
    data = f.read()
    print("-----" * 5)




List with intervalls
-> File name
->



print(inteListTuble(0 , 50))








for b_line in breakList:
    lastLine = b_line
    print(str(prevLastLine) + "-"+ str(lastLine))
    prevLastLine = b_line + 1
    fileName  = (str(prevLastLine).zfill(4) + "-" + str(lastLine).zfill(4) + "_BusinessRegister-Email.csv")
    file = pathlib.Path.cwd().joinpath("InTraCenTestFiles" , fileName )
    with open(file, 'w') as nf:
        nf.write(contentToWrite)



'''
if (1000 - lastLine < 50):
    f.name(prevLastLine "-" +  lastLine + "_BusinessRegister-Email.csv)

else:
    f.name(prevLastLine "-" +  lastLineOfFile + "_BusinessRegister-Email.csv)

'''