# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:16:50 2016

@author: Rainer Warth raine_kd2ek0t

@course: EDX 600.1 Intro to Python
"""


# Get input

month =    1
balance = 0
unpaidBal = 0             
monthlyPaymentRate = 0
annualInterestRate = 0

balance = 484   # 42,  int(input("Enter an balance in USD: "))
annualInterestRate =  0.2  #  0.2   # float(input("Annual interst rate [%]: "))
monthlyPaymentRate = 0.04  # 0.04   #float(input("Monthly payment rate  [%: "))

# functions

def monthStatement(month, balance):
    print("\Month {} remaining balance: {}".format(month, balance))

def addInterest(annualInterestRate, balance):
	return balance * ( 1 + annualInterestRate / 12)

def newBalance(monthlyPaymentRate, balance):
    minMonthPayment = balance * monthlyPaymentRate
    return balance - minMonthPayment
    
# main program

print("Test Case 2:")

for month in range(1, 13, 1):
	balance = addInterest(annualInterestRate, balance)
	balance = newBalance(monthlyPaymentRate, balance)
	# monthStatement(month, round(balance, 2))

print("Remaining balance: ", round(balance, 2))