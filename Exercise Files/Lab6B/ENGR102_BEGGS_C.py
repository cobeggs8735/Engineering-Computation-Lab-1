#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:47:40 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: 509
# Assignment: Lab6B (c)
# Date: 23 February 2019

# Divisors
"""
for i in range(1, 101):
    #Finding the divisor
    for n in range (2, i):
        if (i % n) == 0:
            print (n, "divides", i)
"""
# Start at 2
i = 2
while i <= 100: # End at 100
    n = 2 #Starting divisor
    while n <= i:
        if (i % n) == 0: # Find a number without a remainder
            print (n, "divides", i) # Output divisors
        n += 1 # Increment divisor
    i += 1 # Increment dividend
    