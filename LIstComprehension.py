#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn list comprehension and for loops.
#      Ref: https://realpython.com/lessons/filtering-ii-loop-example/
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------



squares = [x * x for x in range(10)]
print(squares)



squaresFor = []
for x in range(10):
    squaresFor.append(x * x)
print(squaresFor)



