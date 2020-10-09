#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 04-10-2020 Previous: -- First: --
#    Goals: Learn map()
#      Ref: https://realpython.com/python-map-function/
#      Ref: https://docs.python.org/3/library/functional.html?highlight=map%20function%20iterable
#      Ref: 
#      Ref: 
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --

print("The following examples are from an realpython article")
print("THe following code can be replaced by with map()")

numbers = [1, 2, 3, 4, 5]
squared = []

for num in numbers:
    squared.append(num ** 2)

print(squared)
# result: [1, 4, 9, 16, 25]

print("Here the map() version")

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

print(list(squared))
# resutl: [1, 4, 9, 16, 25]