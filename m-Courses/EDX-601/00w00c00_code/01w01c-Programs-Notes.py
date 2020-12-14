# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 08:39:51 2016

@author: raine_u

@description: Lecture 1 of EDX - Python course 600.
"""

print('-----' * 3)
print('turing complete language, can perform all basic operations)
print('turing showed that only 6 operations are necessary to perform computations)
print('syntax, static semantic, semantic)


print('-----' * 3)


# even and odd execise to learn if-else statements

x = int(input('Enter an integer: '))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')

# nested conditional

print('-----' * 3)
print('Now I test if x is divisible by 2 and 3 - nested conditional')
if x%2 == 0:
    if x%3 == 0:
        print('')
        print('Divible by 2 and 3')
    else:
        print('Divible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')
print('Done with nested conditional')   

print('-----' * 3)
print('Compound booleans')
x = int(input('Enter an integer x: '))
y = int(input('Enter an integer y: '))
z = int(input('Enter an integer z: '))

if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is leas')

    

# compond booleans