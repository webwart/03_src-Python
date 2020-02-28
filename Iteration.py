#  REF:  www.edx.org Python course
#  class 2
#

# edx.org, week 2, lecture 3, first example in lecture
#The code squares the value of x by repetivie addition
x = 3
ans = 0
itersLeft = x

while itersLeft != 0:
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + "*" + str(x) + "=" + str(ans))
print("Finished square x")

# edx.org, week 2, lecture 3, execise in lecture
#The code squares the value of x by repetivie addition
print("--- Pay attention to variable in the loop,  increased in the last loop !---")
num = 0
while num <= 5:
    print (num)
    num += 1

print("Outside of loop")
print (num)
print("--- End: Pay attention to variable...---")

# edx.org, week 2, lecture 3, execise in lecture
# use of "while True" and break statement
print("--- use of -while True- and -break- statement- ---")
num = 10
while True:
    if num < 7:
        print ("Breaking out of loop")
        break
    print (num)
    num -= 1
print ("Outside of loop")
print("--- End: -while True- break -tatement- ---")
print("--- Start: -New Problem- ---")

iter = 1
summe = 0
en = 3
while (iter <= en):
    summe = iter + summe
    iter = iter + 1
    print(summe)

# Here is one of a few ways to solve this problem:
total = 0
current = 1
end = 5
while current <= end:
    total += current
    current += 1
print(total)    

