# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:55:42 2016

@author: raine_u
"""

# Bindings
# How to swap bindings

x = 4
y = 5

temp = x     # now temp is also 4

x = y        # now x is 5 and y is still 5
y = temp     # now y is for which it get s from temp which it got from x


# Concatenating strings
# Overloading the "+" plus operator. The type of object tells operator what to do

first = "Rainer"
last = "Warth"
name = first + " " +last
print(name)

# OVerloding the "*" multiply oerator

print("---" * 3)

# Indexing srtrings

dna = "AGATCG"
print(dna[2])
print(dna[2:4])   # returns index 2 to the index before 4
print(dna[:3])
print(dna[4:])
