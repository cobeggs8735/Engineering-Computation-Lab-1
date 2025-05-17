#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:27:07 2019

@author: colemanbeggs
"""

print ()
print ("Coleman Beggs")
print ("ENGR: 102-509")
print ("I'm a world champion robot driver.")

import math

"""
Fake News
# Find position at time 50
# Output position on 3 seperate lines
# (x,y,z) = (x0,y0,z0) + t * (a,b,c)
# a = x2-x1 b = y2-y1 c = z2-z1
# f(x,y) = px+qy+k
# z-z0 = p(x-x0) + q(y-y0)
"""
# fraction = (t-t1)/(t2-t1)
# x = x1 + fraction * (x2-x1)
# y = y1 + fraction * (y2-y1)
# z = z1 + fraction * (z1-z2)

print ()

t13 = 13 #Time
x13 = 1 #x
y13 = 3 #y
z13 = 7 #z

t84 = 84 #Time
x84 = 23 #z
y84 = -5 #y
z84 = 10 #z

t50 = 50
h50 = (t50 - t13) / (t84 - t13)

x50 = x13 + h50 * (x84-x13)
y50 = y13 + h50 * (y84-y13)
z50 = z13 + h50 * (z84-z13)

"""
x0 = -285

xVector = x84 - x13 #Vector Value
yVector = y84 - y13 #Vector Value
zVector = z84 - z13 #Vector Value

x50 = x0 + (84 * xVector)
"""
print ("At time 13", "(", x13,",", y13, ",", z13, ")")
print ("At time 84", "(", x84, ",", y84, ",", z84, ")")
print ("X at time 50 =", x50)
print ("Y at time 50 =", y50)
print ("Z at time 50 =", z50)
