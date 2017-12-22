#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:49:44 2017

@author: efrem
"""

def getBalanceAfterYear(balance, annualInterestRate, monthlyPayment):
    '''
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal
    monthlyPayment: fixed monthly payment
    
    returns: balance remaining on the credit card
    '''
    
    monthlyInterestRate = annualInterestRate / 12.0
    
    curMonth = 1
    lastMonth = 12
    
    while curMonth <= lastMonth:
        ub = balance - monthlyPayment
        balance = round(ub + (monthlyInterestRate * ub), 2)
        curMonth += 1
    return balance


balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0

lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

remainingBalance = balance
    
while(remainingBalance > .4 or remainingBalance < 0):
    curPayment = round((upperBound + lowerBound) / 2, 2)
    remainingBalance = getBalanceAfterYear(balance, annualInterestRate, curPayment)
    if remainingBalance > 0:
        lowerBound = curPayment 
    else:
        upperBound = curPayment

print("Lowest Payment: " + str(curPayment))
