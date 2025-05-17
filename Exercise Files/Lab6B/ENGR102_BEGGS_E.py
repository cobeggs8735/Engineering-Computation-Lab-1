#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:48:29 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: 509
# Assignment: Lab6B (e)
# Date: 23 February 2019

#Formula:
# 4 Sum ((-1)**k) / (2*k +1)

# For loop for summation
import math

terms = 1
err = 100

while err > 1e-6:
    guess_val = 0
    for k in range(terms):
        num = (-1)**k # Numerator
        den = (2 * k) + 1 # Denominator
        guess_val = guess_val + (4 * num / den)
    err = abs(math.pi - guess_val)
    terms += 1
print (terms, "Terms")
print ("Module value:", math.pi, end = ", ")
print ("Estimated value:" , end = ", " )
