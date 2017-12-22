#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:17:07 2017

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


balance = 3926
annualInterestRate = 0.2

curPayment = 0
remainingBalance = 1

while(remainingBalance > 0):
    curPayment += 10
    remainingBalance = getBalanceAfterYear(balance, annualInterestRate, curPayment)

print("Lowest Patment: " + str(curPayment))