#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:38:00 2019

@author: colemanbeggs
"""

import math
print ()

#Part 1 &2
print ("Part 1 &2")

tolerance = .01

a = 1/7
print(a)
b = a*7
print(b)

if abs(1 - b) <= tolerance:
    print ("Is (1/7)*7 the same as 1.0? True")
    
else:
    print ("Is (1/7)*7 the same as 1.0? False")

a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)

if abs(1 - e) <= tolerance:
    print ("Is (2/7)+ (5/7) the same as 1.0? True")
    
else:
    print ("Is (2/7)+(5/7) the same as 1.0? False")

x = math.sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)

if abs(z - y) <= tolerance:
    print ("Is x*x*3 the same as x*3*x? True")

else:
    print ("Is x*x*3 the same as x*3*x? False")

#Part 3
print ()
print ("Part 3")

a = math.sqrt(3.0) * math.sqrt(3.0)
b = math.sqrt(9.0)

print (a)
print (b)

if abs(a - b) <= tolerance:
    print ("a = b: True")
else:
    print ("a = b: False")
    
x = math.sqrt(25.0)
y = math.sqrt(5.0) * math.sqrt(5.0)
print (x)
print (y)

if abs(x - y) <= tolerance:
    print ("x = y: True")

else:
    print ("x = y: False")
