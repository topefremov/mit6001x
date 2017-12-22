#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:17:28 2017

@author: efrem
"""

from math import tan, pi

def polysum(n, s):
    '''
    n: number of sides of polygon
    s: length of sides
    
    returns: Sum of the area and square of the perimeter
             of the regular polygon rounded to 4 decimal
             places
    '''
    area = (0.25*n*(s**2))/(tan(pi/n))
    perimeter = n*s
    return round(area + perimeter**2, 4)