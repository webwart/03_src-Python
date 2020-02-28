#%%
stwe = "Python"
print(stwe[2:5])
print(stwe[:5])
print(stwe[-6:])
print(stwe[:-1])
print(stwe[-1:])
print(stwe[0:])
print(stwe[1:])
print(stwe[2:])
print(stwe[3:])
print('''   
  0  | 1  | 2  | 3  | 4  | 5  ")
   P |  Y |  T |  H |  O |  N ")
 -6  |-5  |-4  |-3  |-2  |-1  ")
        ''')
print(stwe[-3:])
print("[-3:] --" , stwe[-3:])
print("[-1:] --" , stwe[-1:])
print("[-3:5] --" , stwe[-3:5])  # THis can cause confusion

print(" 0p-6 | 1y-5 | 2t-4 | 3h-3 | 4o-2 | 5n-1 ")
for n in range(7):
    if n == 0:
        pass
    else:
        print("[-", n , ":] --" , stwe[-n:])
print("------")
for n in range(6):
    print("[ ", n ,":] --" , stwe[n:])


