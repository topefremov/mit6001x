#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 09:07:51 2017

@author: efrem
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    index = len(aStr) // 2
    if len(aStr) == 0:
        return False
    elif char == aStr[index]:
        return True
    elif char < aStr[index]:
        return isIn(char, aStr[:index])
    else:
        return isIn(char, aStr[index+1:])