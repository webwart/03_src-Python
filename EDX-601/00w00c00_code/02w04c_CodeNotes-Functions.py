# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:07:51 2016

@author: raine_u
@course: Edx Python 6.00.1x -Introduction to computer Science and Programming Using Python
@week: 2 Simple Programs
@class: 4. Funktions

"""

# Abstraction: do not need to know how it works. Standard interace
# Decompostion: Different devices are synchronized to work together
# Modules are self-contained, break up code, reusable, keep code organized, keep code coherent
# We start with functions, later we use classes.


print("----" * 4)
print("Exercise 1 - Problem 1")
print("- - " * 4)

print("Returns a bolean value")
def d(x, y):
   '''
   x: Can be int or float.
   y: Can be int or float.
   '''
   return x > y

   
print("Returns a nothing or none Type")
def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
   

'''
Video Calling Functions
00:17 - Variable Scope, formal parameter and actual parameter

>N: REVEIWE video Calling Functions
>N: Use pythontutor.com
'''

print("----" * 4)
print("Video Example 1 - 00:41 Calling Functions")
print("- - " * 4)

def f2(x):
    x = x + 1
    print('in f(x): x = ', x)
    return x
x = 3
z = f2( x )
print("value of f(x) assigend to z:", z)

'''
Video Calling Functions
06:16 - Return vs. print
'''
print("----" * 4)
print("Video Example 2 - 08:50 Calling Functions")
print("- - " * 4)

def func_a():
    print('inside func_a')
    
def func_b(y):
    print('inside func_b')
    return y
    
def func_c(z):
    print('inside func_c')
    return z()
    
print(func_a())
print(5 + func_b(2))
print(func_c(func_a)) 

'''
Video Calling Functions
10:25 - Inside a function I can access a variable defined outside, but not modify
'''

'''
Exercise: square
Write a Python function, square, that takes in one number and returns the square of that number.
This function takes in one number and returns one number.
'''
print("----" * 4)
print("Exercise Square" )
print("- - " * 4)

def square(x):
    '''
    x: int or float.
    '''
    return x**2

print('Testing square function with value: 3')
print('Result:', square(3))

# >N: 13:24 

# >N: Exercise: fourth power



print("----" * 4)
print("Exercise gcd Iter" )
print("- - " * 4)

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)
    print(" ")
    print(testValue)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue


         
print(gcdIter(120, 10))


print("----" * 4)
print("Exercise gcd Recur" )
print("- - " * 4)



def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)
    
    
print(gcdRecur(10, 120))

print("----" * 4)
pritn("W2-C4 Functions )
print("Video - Fibonaci")
print("- - " * 4)


print("----" * 4)
print("Video - Example Recursion on non-numerics")
print("- - " * 4)


print("----" * 4)
pritn("W2-C4 Functions")
print("Video - Fibonaci")
print("- - " * 4)



