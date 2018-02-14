#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:41:30 2018

@author: efrem
"""

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    
    assert len(word) > 1, "Length of word must be greater then 1"
    assert str.isalpha(word), "Word must contain only alphabetic characters"
    
    # to get score for letter from ASCII number (a = 1, b = 2, ..., z = 26)
    magicNum = 96
    wordCopy = str.lower(word)
    letterScores = []
    curIndex = 0
    while curIndex < len(word):
        letterScores.append((ord(wordCopy[curIndex]) - magicNum) * curIndex)
        curIndex += 1
    
    twoHighestScores = sorted(letterScores)[-2:]
    return f(twoHighestScores[1], twoHighestScores[0])