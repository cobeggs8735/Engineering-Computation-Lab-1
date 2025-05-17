#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:21:02 2019

@author: colemanbeggs
"""

import math
import sympy

#user input
A = 2 #float(input('type the first coefficient:'))
B = 3 #float(input('type the second coefficient:'))
C = 1 #float(input('type the third coefficient:'))
D = -4 #float(input('type the fourth coefficient:'))

a = sympy.Symbol('a')

def f(a):
	return A*(math.sin(a))**3+B*(math.tan(a))**2+C*(math.cos(a))+D

x = float(input('Enter a value for x:'))

lim = sympy.limit(f(a), a, x)

print ("Limit is:", lim)






























