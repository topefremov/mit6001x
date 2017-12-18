#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:36:18 2017

@author: efrem
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    
    iter = exp - 1
    result = base
    while(iter != 0):
        result *= base
        iter -= 1
        
    return result