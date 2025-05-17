#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:48:00 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: 509
# Assignment: Lab6B (d)
# Date: 23 February 2019

# Series

#Formula:
# 4 Sum ((-1)**k) / (2*k +1)

# For loop for summation
import math

terms = 1
i = 1
guess_val = 0 # Estimated Value
for k in range(terms):
    num = (-1)**k # Numerator
    den = (2 * k) + 1 # Denominator
    guess_val = guess_val + (4 * num / den)
print ("Module value: ", math.pi, end = ", ")
print ("Estimated value: ", guess_val, end = ", ")
print (terms, "Terms")

terms = 10
i = 1
guess_val = 0
for k in range(terms):
    num = (-1)**k # Numerator
    den = (2 * k) + 1 # Denominator
    guess_val = guess_val + (4 * num / den)
print ("Module value: ", math.pi, end = ", ")
print ("Estimated value: ", guess_val, end = ", ")
print (terms, "Terms")

terms = 100
i = 1
guess_val = 0
for k in range(terms):
    num = (-1)**k # Numerator
    den = (2 * k) + 1 # Denominator
    guess_val = guess_val + (4 * num / den)
print ("Module value: ", math.pi, end = ", ")
print ("Estimated value: ", guess_val, end = ", ")
print (terms, "Terms")

terms = 1000
i = 1
guess_val = 0
for k in range(terms):
    num = (-1)**k # Numerator
    den = (2 * k) + 1 # Denominator
    guess_val = guess_val + (4 * num / den)
print ("Module value: ", math.pi, end = ", ")
print ("Estimated value: ", guess_val, end = ", ")
print (terms, "Terms")

terms = int(1e6)
i = 1
guess_val = 0
for k in range(terms):
    num = (-1)**k # Numerator
    den = (2 * k) + 1 # Denominator
    guess_val = guess_val + (4 * num / den)
print ("Module value: ", math.pi, end = ", ")
print ("Estimated value: ", guess_val, end = ", ")
print (terms, "Terms")

terms = int(1e9)
i = 1
guess_val = 0
for k in range(terms):
    num = (-1)**k # Numerator
    den = (2 * k) + 1 # Denominator
    guess_val = guess_val + (4 * num / den)
print ("Module value: ", math.pi, end = ", ")
print ("Estimated value: ", guess_val, end = ", ")
print (terms, "Terms")
