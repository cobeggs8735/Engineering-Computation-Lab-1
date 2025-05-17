#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coleman Beggs

UIN: 326009580

ENGR: 102 - 509

I'm a former world champion robot driver.
"""

import math

#Limits
print ()

# 5 * x / (x - 2)
print ("This shows the evaluation of 5 * x / (x - 2) evaluated close to x = 1")
print ("My guess is -5.0")

print (5 * 1.1 / (1.1 - 2)) #1.1
print (5 * 1.01 / (1.01 - 2)) #1.01
print (5 * 1.001 / (1.001 - 2)) #1.001
print (5 * 1.0001 / (1.0001 - 2)) #1.0001
print (5 * 1.00001 / (1.00001 - 2)) #1.00001
print (5 * 1.000001 / (1.000001 - 2)) # 1.000001
print (5 * 1.0000001 / (1.0000001 - 2)) #1.0000001

# f(x) = sin(x)/x
print ()
print ("This is an evaluation of f(x) = sin(x)/x evaluated close to x = 0")
print ("My guess is 1.0")

x = 1
fx = math.sin(x) / x
print ("f(1)    =",fx) 

x = 1E-1
fx = math.sin(x) / x
print ("f(1E-1) =", fx)

x = 1E-2
fx = math.sin(x) / x
print ("f(1E-2) =", fx)

x = 1E-3
fx = math.sin(x) / x
print ("f(1E-3) =", fx)

x = 1E-4
fx = math.sin(x) / x
print ("f(1E-4) =", fx)

x = 1E-5
fx = math.sin(x) / x
print ("f(1E-5) =", fx)

x = 1E-6
fx = math.sin(x) / x
print ("f(1E-6) =", fx)

x = 1E-7
fx = math.sin(x) / x
print ("f(1E-7) =", fx)

# g(x) = (1 - cos(x))/x**2
print ()
print ("This is an evaluation of g(x) = (1 - cos(x))/x**2 evaluated close to x = 0")
print ("My guess is 1.0")

x = 1
gx = (1 - math.cos(x)) / x**2
print ("g(1)    =", gx)

x = 1E-1
gx = (1 - math.cos(x)) / x**2
print ("g(1E-1) =", gx)

x = 1E-2
gx = (1 - math.cos(x)) / x**2
print ("g(1E-2) =", gx)

x = 1E-3
gx = (1 - math.cos(x)) / x**2
print ("g(1E-3) =", gx)

x = 1E-4
gx = (1 - math.cos(x)) / x**2
print ("g(1E-4) =", gx)

x = 1E-5
gx = (1 - math.cos(x)) / x**2
print ("g(1E-5) =", gx)

x = 1E-6
gx = (1 - math.cos(x)) / x**2
print ("g(1E-6) =", gx)

x = 1E-7
gx = (1 - math.cos(x)) / x**2
print ("g(1E-7) =", gx)

# h(x) = (1 + (1/x))**x
print ()
print ("his is an evaluation of h(x) = (1+(1/x))**x evaluated close to x = ∞")
print ("My guess is 3.0")

x = 1
hx = math.pow((1 + (1 / x)),x)
print ("h(1)   =", hx)

x = 1E1
hx = math.pow((1 + (1 / x)),x)
print ("h(1E1) =", hx)

x = 1E2
hx = math.pow((1 + (1 / x)),x)
print ("h(1E2) =", hx)

x = 1E3
hx = math.pow((1 + (1 / x)),x)
print ("h(1E3) =", hx)

x = 1E4
hx = math.pow((1 + (1 / x)),x)
print ("h(1E4) =", hx)

x = 1E5
hx = (1 + (1 / x))**x
print ("h(1E5) =", hx)

x = 1E6
hx = math.pow((1 + (1 / x)),x)
print ("h(1E6) =", hx)

x = 1E7
hx = math.pow((1 + (1 / x)),x)
print ("h(1E7) =", hx)
