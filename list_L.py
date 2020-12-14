#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn about lists in Python
#      Ref: https://docs.python.org/3/tutorial/introduction.html
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------


squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])   # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list
print(squares[:])    # returns a (shalow) copy or the list
concatSquares = squares + [36, 49, 64, 81, 100]
print("Concataned lists:", concatSquares)
print("------- for loop wih a list")
for x in concatSquares:
             print(x)
             print("-<>-")
print("------ end of for loop with a list")

             
# LIST from edx.org course
# Use the list funciton to copy a list object
# More info to the topix: https://docs.python.org/3.5/library/copy.html
#
print("------")
print("------ EDX.ORG example")
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create a second pointer to areas list. The second pointer is called areas_copy
areas_copy = areas

# Change areas_copy
print("Change in areas_copy...")
areas_copy[0] = 5.0

# Print areas
print("...change also areas, since the two point to the same address in memory")
print(areas)

# I can create a copy of the areas list with the list() function
areas_copy = list(areas)
areas_copy[0]  =  100
print(areas_copy)
