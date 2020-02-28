# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:06:44 2016

@author: raine_u
@description: Supplementary material for EDx.org 600.1
"""
print("-    " * 6)
print("This is a demo of classes in python")
print("===" * 6)
# print("\n")

class MITxStaff(object):
    firstName = ""
    lastName = ""
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
class TA(MITxStaff):
    awesomenessLevel = 0
    
    def __init__(self, firstName, lastName, awesomenessLevel):
        self.awesomenessLevel = awesomenessLevel
        MITxStaff.__init__(self, firstName, lastName)
        
    def toString(self):
        return "{} {} has an awesomeness level of {}".format(self.firstName, self.lastName, self.awesomenessLevel)

Nitish = TA("Nitish", "Mittal", 100)
Jing = TA("Jing", "Ma", 9001)

print(Nitish.toString())
print(Jing.toString())
