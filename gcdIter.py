#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:19:44 2017

@author: efrem
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = a if a < b else b
    
    while (gcd > 1):
        if (a % gcd == 0) and (b % gcd == 0):
            break;
        gcd -= 1
        
    return gcd