#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 08:55:56 2018

@author: efrem
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    result = ()
    tupleLength = len(aTup)
    i = 0
    while (i < tupleLength):
        result = result + (aTup[i],)
        i += 2
    return result
    
