#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn to use strings.
#      Ref: Edx course Computer Science
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------ 

# String examples from the Edx course Computer Science

ex01= "abcd"[2]
print(ex01)
print('-----')
print("abcd"[0:2])
print('-----')
print("abcd"[:2])
print('-----')
print("abcd"[2:])
print("=======")
str1 = 'hello'
str2 = ','
str3 = 'world'
print('-----')
print(str1[0])
print(str1[1])
# print(str1[len(str1)])
print(str1 + str2 + str3)
print(str1 + str2 + ' ' +str3)
print(str3 * 3)
print(str1 == 'hello')
print(str1 == 'HELLO')
print('a' in str3)
str4 = str1 + str3
print('low' in str4)
print(str3[1:3])
print(str3[:3])
print(str3[:-1])
print(str3[1:])
print(str4[1:9])
print(str4[1:9:2])
print(str4[::-1])
