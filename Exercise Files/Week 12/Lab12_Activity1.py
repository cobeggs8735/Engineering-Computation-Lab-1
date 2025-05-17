#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:11:43 2019

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
# Assignment: Lab 12, Activity 1
# Date: 11 April 2019

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def polynomial(coeffs, x):
    return np.polyval(coeffs, x)

def derivative(coeffs):
    return np.polyder(coeffs)

coeffs = []
coeffs_float = [1, 0]
new = 0

print('Enter coefficients ABCD: y = Ax^n + Bx^n-1 + Cx^n-2 + Dx^n-3...')

degree = 'n'
x = 0

'''while new != 'done':
    coeffs.append(new)
    if x > 0:
        new = input('Enter the coefficient for x raised to the n-' + str(x) + ' degree, \n enter "done" when finished: ')
    else:
        new = input('Enter the coefficient for x raised to the n degree, \n enter "done" when finished: ')

    x += 1
    degree = 'degree-'+str(x)
    
coeffs.remove(0)
'''
for i in range(len(coeffs)):
    x = float(coeffs[i])
    coeffs_float.append(x)

coeffs_array = np.array(coeffs_float)

xVals = np.arange(-15, 15)

function = polynomial(coeffs_array, xVals)
deriv1 = polynomial(derivative(coeffs_array), xVals)
deriv2 = polynomial(derivative(derivative(coeffs_array)), xVals)

'''FIXME: Certain odd degree polynomials have a complex number error for local extrema'''

x = sp.symbols('x')
zeroes = np.real(np.array(sp.solvers.solve(polynomial(derivative(coeffs_array), x))))

plt.plot(xVals, function, 'r-', label='Function')
plt.plot(xVals, deriv1, 'g--', label='1st Derivative')
plt.plot(xVals, deriv2, 'b.-', label='2nd Derivative')
plt.plot(zeroes, polynomial(coeffs_array, zeroes),'k.', label='Local Extrema')
plt.ylim([-50, 50])
plt.legend(loc='best')
plt.grid()
