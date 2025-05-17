#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:47:04 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: 509
# Assignment: Lab6B (b)
# Date: 23 February 2019
# Averaging Measurements

n1 = float(input("Enter a positive measurement: "))
i = 0
n2 = 0
n4 = n1
# User inputs an unknown amount of measurements
if n1 > 0:
    while n2 >= 0:
        i += 1    
        n2 = float(input("Enter another number (enter negative to stop): "))
    
    # Negative measurement is used to end inputs (not proccessed)
        if n2 > 0:
            n3 = 0
            n4 += n2
    # Find the max and min measurement
            if n1 < n2:
                Min = n1
            elif n2 < n3:
                Min = n2
            if n1 > n2:
                Max = n1
            elif n2 > n3:
                Max = n2
            n3 = n2
    
        else:
            n4 = n4
            # Average the measurements
            avg = n4 / i
            break
else:
    print ("Invalid input")
    
print ("Min =", Min, end = ", ")
print ("Max =", Max, end = ", ")
print ("Average =", avg, end = ", ")
