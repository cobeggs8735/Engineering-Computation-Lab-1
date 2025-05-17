#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:12:56 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: 509
# Assignment: Lab6B (a)
# Date: 23 February 2019

#The Collatz Conjecture


# Take a positive integer from the user

n = int(input("Enter a postive integer: ")) # Number Input from user
iterations = 0
print (n)

while n > 1:
    iterations += 1
# If even number is divided by 2
    if (n % 2) == 0:
        n /= 2
        print (n, end=' ')

# If odd number 3n + 1

    elif (n % 2) > 0:
        n = (3 * n) + 1
        print (n, end=' ')

    else:
        print ("Invalid input")
    
print ()

# Output iteration it took to get to one

print ("Conjecture took", iterations, "iterations")


"""
Test Cases:
    n = 5, 5 iterations
    n = 7, 16 iterations
    n = 9, 16 iterations    
"""

