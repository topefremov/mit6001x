#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:41:45 2017

@author: efrem
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''    
    if exp == 0:
        return 1
    
    return base*recurPower(base, exp - 1)