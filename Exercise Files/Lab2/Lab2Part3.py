#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:21:20 2019

@author: colemanbeggs
"""

print ()
print ("Coleman Beggs")
print ("ENGR102-509")

x1 = 2 # X1 Value
x2 = 10 # X2 Value
y1 = 3 # Y1 Value
y2 = 12 # Y2 Value
m = (y2 - y1) / (x2 - x1) # Slope of the line
b = y2 - (m * x2) # Y-intercept of the line

X_input = input("Please enter an 'x' value number between the two given points (2, 3) & (10, 12) : ")
X_input = float(X_input)

Y = (m * X_input) + b # Linear equation of th eline

print ()
print ("X = ", X_input) #Prints X value
print ("Y = ", Y) # Prints Y value
print ("New Point :", "(", X_input, ", ", Y, ")")