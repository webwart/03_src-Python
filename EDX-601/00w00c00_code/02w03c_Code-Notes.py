# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 08:47:37 2016

@author: raine_u


@course: Edx Python 6.00.1x -Introduction to computer Science and Programming Using Python
@week: 2 Simple Programs
@class: 3. Simple Algorithems 

"""

print("----" * 4)
print("Exercise 1 - Problem 1")
print("----" * 4)

iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every character, cluding spaces and coma
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

print("----" * 4)
print("Exercise 1 - Problem 2")
print("----" * 4)

iteration = 0

while iteration < 5:
    count = 0
    # the variable 'letter' in the loop stands for every character, cluding spaces and coma
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

print("----" * 4)
print("Exercise 1 - Problem 3")
print("----" * 4)

iteration = 0

while iteration < 5:
    count = 0
    # the variable 'letter' in the loop stands for every character, cluding spaces and coma
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
#-------------------------------    
print("----" * 4)
print("Exercise 2 - Problem 1")
print("----" * 4)

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
    
print("----" * 4)
print("Exercise 2 - Problem 2")
print("----" * 4)
print("Code will enter a loop and I commented it out")
'''
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break                 # remove else: guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
'''
print("----" * 4)
print("Exercise 2 - Problem 3")
print("----" * 4)

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
    
# Printing in one line

print("Hi", end=' ')
print("there")


# Learn about bidirectional search 

print("----" * 4)
print("Exercise - Guess my number")
print("----" * 4)

# Learn about floats. Explaination by Binary Digits
# Floats cannot be compared use: abs(Floatvariable) or print(Floatvariable)
    
# Newton Raphson


# Iterative Algorithems
# - Use a looping contruct to generate guesses, then check and continue
# - Generating guesses:  Exhaustive enumeration, Bisection search, Newton-Raphson (for root finding)




