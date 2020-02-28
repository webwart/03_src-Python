# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:14:36 2016

@author: raine_u
"""
print("---" * 3)
print("Learn range()")
num = 10
for num in range(5):
    print(num)
print(num)

print("---" * 3)
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor, "->", type(num/divisor))
print("---" * 3)
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
print("---" * 3)
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

print("---" * 3)

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 