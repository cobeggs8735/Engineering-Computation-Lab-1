#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:42:32 2019

@author: colemanbeggs
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Coleman Beggs
# Andrew Pool
# Cody Knight
# Andrew Mitchell
# Section: ENGR102-509
# Assignment: Lab 12, Activity 2
# Date: 11 April 2019

import numpy as np
#import matplotlib.pyplot as plt

def polynomial(coeffs, x):
    return np.polyval(coeffs, x)

def integral(n, riemannType, start, end, coeffs):
    if riemannType == 'right': # Right-hand Reimann sum
        points = np.arange(start+((end-start)/n), end, (end-start)/n) #Right
        riemannSum = sum(polynomial(coeffs, points) * (end-start)/n)
    
    elif riemannType == 'left': # Left-hand Reimann sum
        points = np.arange(start, end, (end-start)/n) #Left
        riemannSum = sum(polynomial(coeffs, points) * (end-start)/n)
    
    else: #Mid-point Reimann sum
        points = np.arange(start+(((end-start)/n)/2), end, (end-start)/n) #Mid-Point
        riemannSum = sum(polynomial(coeffs, points) * (end-start)/n)
    return riemannSum

coeffs = []
coeffs_float = [1, 0]
new = 0

#while new != 'done' :
	#coeffs.append(new)
	#new = str(input("Enter coefficients of polynomial one at a time, enter 'done' when finished : "))
    
#coeffs.remove(0)

for i in range(len(coeffs)):
    x = float(coeffs[i])
    coeffs_float.append(x)

coeffs_array = np.array(coeffs_float)

# Bounds and Closed Interval
n = 10 # bisections of area
start = 0 #float(input("Enter the lower bound of the interval to integrate: ")) # Lower bound of the integral
end = 10 #float(input("Enter the upper bound of the interval to integrate: ")) # Upper bound of the intergral)
riemannType = input("Enter the type of Riemann sum ('left', 'right', or 'mid'): ")
print(integral(n, riemannType, start, end, coeffs_array))
# Loop to determine Convergence
error = 1000
while error >= 10e-6:
    error = abs(integral(n, riemannType, start, end, coeffs_array) - integral(n+1, riemannType, start, end, coeffs_array))
    n += 1

print("\nApproximate integral of function is:", integral(n, riemannType, start, end, coeffs_array))
print("Program took", n, "iterations until convergence")
