#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:00:11 2018

@author: efrem
"""

def getSublists(L, n):
    subLists = []
    curIndex = 0
    while True:
        subList = L[curIndex:curIndex + n]
        if len(subList) < n:
            break
        subLists.append(subList)
        curIndex += 1
    
    return subLists
            
    