#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 02-07-2020
#    Goals: Learn lambda, map, filter and reduce
#      Ref: https://www.youtube.com/watch?v=cKlnR-CB3tk from Joe James
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------

# lambda functions can be writen as a normal function

def doubleX(x):
    return x * 2

print(doubleX(4))

x , y = 4 , 5

mPlus = lambda x , y: x + y

print(mPlus(x , y))