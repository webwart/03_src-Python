# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 13:06:36 2016

@author: raine_u
"""


'''
print("practise while loops")

repeat = int(input("give me number lower than 10: "))
print("repeate ", repeat)

x= 0
while x < repeat:
    x = x + 1
    print("counter  ", x )

    
print("I am done")
'''

print(" ")
print("Now I practise for loopes")

'''
size = int(input("Upper limit "))

for x in range(size, 10, 2):
    print("default", x)
print("i am done")
'''

print("Now I use a for loop with a series of objects")

xlist = list(range(5))
print(xlist)

print("---" * 3)
print("- Range and For- statement")
print("---" * 3)

for count in range(2, 12, 2):
    print(count)
print("Goodbye!")

# Here is another:
print("Hello!")
for num in range(10, 0, -2):
    print(num)

# Build the summe of a number

end = 5     # This is the input
total = 0
for next in range(1, end+1):
    total += next
print(total)

# Here is another:
total = end
for next in range(end):
    total += next
print(total)
    


print("Exercise to use if and -or- ")

varA = "hello"
varB = "3"

if type(varA) == str or type(varB) == str:
    print('- >string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    # If none of the above conditions are true,
    # it must be the case that varA < varB
    print('smaller')
    
    
print("---" * 3)

num = 0
while num <= 5:
    print(num)
    num += 1
print("Outside of loop")
print(num)

print("---" * 3)
print("- Undertanding the break statement")
print("---" * 3)

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')


print("---" * 3)
print("- Summing up the numbers of a series")
print("---" * 3)
    

# Here is one of a few ways to solve this problem:
total = 0
current = 1
end = 10
while current <= end:
    total += current
    current += 1

print(total)
