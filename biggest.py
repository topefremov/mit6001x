#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:03:39 2018

@author: efrem
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    
    resultKey = None
    biggestLength = 0
    for key, list in aDict.items():
        if len(list) >= biggestLength:
            biggestLength = len(list)
            resultKey = key
    return resultKey
