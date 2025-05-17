#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:14:32 2019

@author: colemanbeggs
"""

#Input a number and tell user the largest one

# First number

x = float(input("Input a number: ", )) #First number

# Second number

y = float(input("Input a differnt second number: ", )) #Second number

# Third number

z = float(input("Input a different third number: ", )) #Third number

# Which is largest

print ("Which number is largest?")

if (x > y) and (y > z):
    print (x, "is the largest number")
elif (x > z) and (z > y):
    print (x, "is the largest number")
elif (y > x) and (x > z):
    print (y, "is the largest number")
elif (y > z) and (z > x):
    print (y, "is the largest number")
elif (z > y) and (y > x):
    print (z, "is the largest number")
elif (z > x) and (x > y):
    print (z, "is the largest number")
else:
    print ("Not a valid set of numbers")