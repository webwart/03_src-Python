#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn use of input()
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------

s = input("What is your name ?")
print(f"Hello {s}")
counter = 0
for n in range(15):
    print(f"-{n} and {s}")
    counter = counter + 1

print("out of loop --------" , end="This is the ende")

print("-----------")

x = 5
m = 1

while m < 5 :
    print(m)
    m = m + 1

print(">>>" + str(m) )
