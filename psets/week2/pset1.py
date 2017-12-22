#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:50:38 2017

Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each 
month.

@author: efrem
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthltInterestRate = annualInterestRate / 12.0


curMonth = 1
lastMonth = 12

while curMonth <= lastMonth:
    ub = balance - (monthlyPaymentRate * balance)
    balance = round(ub + (monthltInterestRate * ub), 2)
    print("Month " + str(curMonth) + " Remaining balance: " + str(balance))
    curMonth += 1

print("Remaining balance: " + str(balance))
