#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:16:40 2019

@author: colemanbeggs
"""

import cmath
import sympy

# Ax^2 + Bx + C

a = float(input("Enter the 'A' in Ax^2 + Bx + C coefficient: ", )) #A value
b = float(input("Enter the 'B' in Ax^2 + Bx + C coefficient: ", )) #B value
c = float(input("Enter the 'C' in Ax^2 + Bx + C coefficient: ", )) #C value
x = sympy.symbols('x')
y = (a * x**2) + (b * x) + c
root1 = (-b+cmath.sqrt(b**2 + (4*a*c)))/2
root2 = (-b-cmath.sqrt(b**2 + (4*a*c)))/2

print (y)
print (root1)
print (root2)

























