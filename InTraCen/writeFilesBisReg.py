
# https://realpython.com/working-with-files-in-python/
#  5766 Lines
# I will use a test file with 1000 lines.
# I  will create files with lines of 70 +- 20



lastLineOfFile = 8
prevLastLine = 1
lastLine = 2
contentToWrite = ""

for breakline in  range(9):
    print(breakline)

print(str(lastLine) + "---->" + line)


with open('0001-0008_BusinessRegister-Email-Test.csv', ) as f:
    for line in f:
        contentToWrite = (contentToWrite + line )
        print(str(lastLine) + "---->" + line)
        lastLine = lastLine + 1
        # f.w
    data = f.read()
    print("-----" * 5)



fileName  = (str(prevLastLine).zfill(4) + "-" + str(lastLine).zfill(4) + "_BusinessRegister-Email.csv")
with open(fileName, 'w') as nf:
    nf.write(contentToWrite)



'''
if (1000 - lastLine < 50):
    f.name(prevLastLine "-" +  lastLine + "_BusinessRegister-Email.csv)

else:
    f.name(prevLastLine "-" +  lastLineOfFile + "_BusinessRegister-Email.csv)

'''