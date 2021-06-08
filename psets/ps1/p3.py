#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:09:14 2021

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. 

For example, if s = 'azcbobobegghakl', then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print;
Longest substring in alphabetical order is: abc

@author: aefremov
"""
#s = "azcbobobegghakl"
#s = "qbrgsldsh"
s = 'abcdefghijklmnopqrstuvwxyz'
longest_substr = ""
cur_substr = ""
for c in s:
    if len(cur_substr) == 0 or cur_substr[-1] <= c:
        cur_substr += c
    else:
        if len(cur_substr) > len(longest_substr):
            longest_substr = cur_substr
        cur_substr = c

if len(cur_substr) > len(longest_substr):
    longest_substr = cur_substr
        

print("Longest substring in alphabetical order is: " + longest_substr)        

