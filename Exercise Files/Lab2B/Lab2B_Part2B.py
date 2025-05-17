#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:42:09 2019

@author: colemanbeggs
"""

print ()
print ("Coleman Beggs")
print ("ENGR: 102-509")
print ("I'm a world champion robot driver.")

import math
import numpy

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

print ("At time 13", "(", x13,",", y13, ",", z13, ")")
print ("At time 84", "(", x84, ",", y84, ",", z84, ")")
print ()

t50 = 50 #time 50
h50 = (t50 - t13) / (t84 - t13) #contsant 50

x50 = x13 + h50 * (x84-x13) # x at time 50
y50 = y13 + h50 * (y84-y13) # y at time 50
z50 = z13 + h50 * (z84-z13) # z at time 50

print ("X at time 50 =", x50)
print ("Y at time 50 =", y50)
print ("Z at time 50 =", z50)
print ("------------------")

t51 = 51 #time 51
h51 = (t51 - t13) / (t84 - t13) #contsant 51

x51 = x13 + h51 * (x84-x13) # x at time 51
y51 = y13 + h51 * (y84-y13) # y at time 51
z51 = z13 + h51 * (z84-z13) # z at time 51

print ("X at time 51 =", x51)
print ("Y at time 51 =", y51)
print ("Z at time 51 =", z51)
print ("------------------")

t52 = 52 #time 52
h52 = (t52 - t13) / (t84 - t13) #contsant 52

x52 = x13 + h52 * (x84-x13) # x at time 52
y52 = y13 + h52 * (y84-y13) # y at time 52
z52 = z13 + h52 * (z84-z13) # z at time 52

print ("X at time 52 =", x52)
print ("Y at time 52 =", y52)
print ("Z at time 52 =", z52)
print ("------------------")

t53 = 53 #time 53
h53 = (t53 - t13) / (t84 - t13) #contsant 53

x53 = x13 + h53 * (x84-x13) # x at time 53
y53 = y13 + h53 * (y84-y13) # y at time 53
z53 = z13 + h53 * (z84-z13) # z at time 53

print ("X at time 53 =", x53)
print ("Y at time 53 =", y53)
print ("Z at time 53 =", z53)
print ("------------------")

t54 = 54 #time 54
h54 = (t54 - t13) / (t84 - t13) #contsant 54

x54 = x13 + h54 * (x84-x13) # x at time 54
y54 = y13 + h54 * (y84-y13) # y at time 54
z54 = z13 + h54 * (z84-z13) # z at time 54

print ("X at time 54 =", x54)
print ("Y at time 54 =", y54)
print ("Z at time 54 =", z54)
print ("------------------")
