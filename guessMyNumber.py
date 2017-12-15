# -*- coding: utf-8 -*-
"""
author: Aleksandr Efremov
"""

low = 0
high = 100

ans = (low + high) // 2

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number " + str(ans) + "?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate " + 
                "the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if (inp == 'c'):
        print("Game over. Your secret number was: " + str(ans))
        break
    elif (inp == 'l'):
        low = ans
    elif (inp == 'h'):
        high = ans
    else:
        print("Sorry, I did not understand your input.")
        continue
    ans = (low + high) // 2

