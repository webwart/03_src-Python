#  REF:  www.edx.org Python course
#  class 2
#
'''
This code does not work ! The raw_input function is depreciated !
Input doe not work, since it convertes all input to string !

varA = raw_input("Type in a value int or string: ")
varB = raw_input("One more time, Type in a value int or string: ")

'''
varA = 945
# varB = "adios"
varB = 10




# == has precendence over or
if type(varA) == str or type(varB) == str:
    print ("string involved")
elif varA > varB:
    print ("bigger")
elif varA == varB:
    print ("equal")
else:
    # If none of the above conditions are true,
    # it must be the case that varA < varB
    print ("smaller")

print("-------Odd and Even numbers--------")
x = int(input("Enter an integer:  "))
if x%2 == 0:
    print("")
    print("--> Even")
else:
    print("")
    print("--> Odd")
print("Done testing for Even and Odd")

print("-------Nested conditionals--------")
x = int(input("Enter an integer:  "))
if x%2 == 0:
    if x%3 == 0:
        print("")
        print("--> Divisible by 2 and 3")
    else:
        print("")
        print("--> Divisible by 2 and not by 3")
elif x%3 == 0:
    print("Divisible by 3 and nob by2")
    
print("Done testing for division by 2 or 3")
