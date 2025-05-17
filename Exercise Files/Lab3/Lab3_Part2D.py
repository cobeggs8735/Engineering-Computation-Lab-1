#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:49:45 2019

@author: colemanbeggs
"""

#a. e-x
#b. xy
#c. sin(x + y)
#d. x/y
#e. x2+y2

import math

# e ** x

x = float(input("Input a value for x: "))
fx = math.exp(-x)

print ("e**x =", fx)

# x * y

x = float(input("Input a value for x: "))
y = float(input("Input a value for y: "))
z = x * y

print ("xy =", z)

# sin (x + y)

x = float(input("Input a value for x: "))
y = float(input("Input a value for y: "))
z = math.sin (x + y)

print ("sin(x+y) =", z)

# x/y

x = float(input("Input a value for x: "))
y = float(input("Input a value for y: "))
z = x / y
print ("x/y =", z)

# x**2 + y**2

x = float(input("Input a value for x: "))
y = float(input("Input a value for y: "))
z = x**2 + y**2
print ("x^2 + y^2 =", z)