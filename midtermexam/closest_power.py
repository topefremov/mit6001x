#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:28:49 2018

@author: efrem
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    power = -1
    smallerClosestPower = 1
    greaterClosestPower = None
    done = False
    while not done:
        power += 1
        result = base** power
        if result <= num:
            smallerClosestPower = power
        else:
            greaterClosestPower = power
            done = True
    if (greaterClosestPower == None or 
        (base** greaterClosestPower - num) >= (num - base** smallerClosestPower)):
        return smallerClosestPower
    else:
        return greaterClosestPower