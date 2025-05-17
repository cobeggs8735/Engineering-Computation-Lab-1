#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:12:56 2019

@author: colemanbeggs
"""

#Part (a)
#The Collatz Conjecture


# Take a positive integer from the user

n = 7 #int(input("Enter a postive integer: ")) # Number Input from user
iterations = 0

while n > 1:
    iterations += 1
# If even number is divided by 2
    if (n % 2) == 0:
        n /= 2

# If odd number 3n + 1

    elif (n % 2) > 0:
        n = (3 * n) + 1

    else:
        print ("Invalid input")

# Output iteration it took to get to one

print ("Conjecture took", iterations, "iterations")


"""
Test Cases:
    n = 5, 5 iterations
    n = 7, 16 iterations
    n = 9
    
"""