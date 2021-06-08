#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:57:01 2021

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:
    
Number of times bob occurs is: 2

@author: aefremov
"""
s = "azcbobobegghakl"
word_length = len(s)
bob_count = 0
for i in range(word_length - 2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        bob_count += 1
print("Number of times bob occurs is: " + str(bob_count))        
