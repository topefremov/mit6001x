#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:26:48 2018

@author: efrem
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flattened = []
    for el in aList:
        if isinstance(el, list):
            flattened = flattened + flatten(el)
        else:
            flattened.append(el)
    return flattened