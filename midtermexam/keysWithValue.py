#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:08:01 2018

@author: efrem
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    result = []
    for key in aDict:
        if aDict[key] == target:
            result.append(key)
    
    return sorted(result)