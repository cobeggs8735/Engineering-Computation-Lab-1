#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:24:42 2019

@author: colemanbeggs
"""

"""# User Input Section
#Circle 1
#x1, y1, r1
x1 = float(input("Enter x location for C1",))
y1 = float(input("Enter y location for C1",))
r1 = float(input("Enter radius for C1"))
#Circle 2
#x2, y2, r2
x2 = float(input("Enter x location for C2",))
y2 = float(input("Enter y location for C2",))
r2 = float(input("Enter radius for C2",))
# Do some math section
#Ugh!

# Comparision check
if :#test condition
    #Touching
elif :#test condition
    #Not Touching
else:
    #Overlap
    """
"""
# Fibonacci sequence    
#1. write program to get fibonnaci series between 0 to 500
    
# define the iterand
    
# use a while loop to iterate to 500
    
# create different variables for the three different fibonacci sequence numbers


#starts at 1
# then 1
# then 2
# then 3
fib1 = 1
fib2 = 1
print (fib1)
print (fib2)
fib3 = fib1 + fib2
print (fib3)
while fib3 < 500:
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2
    if fib3 > 500:
        break
    print (fib3)
"""
"""import math

#Macluarurin Series

# User provides an angle the equation is in radians (ang)
#ang = float(input("Input an angle: "))

# User input number of terms  (n)
#n = int(input("Input a number of terms to avaluate: "))

# Use for loop to calculate
### math.factorial()
sinx = 0
for i in range(n):
    #print (i)
    totalx = ((-1)**n / math.factorial(2*n +1)) * math.pow(ang, 2*n +1)
    sinx = totalx + +sinx
    print (sinx)
"""



import math
# estimate sin using mac series
    
#input angle in degrees
angle = float(input("Enter angle in degree: "))
#input number of terms
#num_terms = int(input("Enter number of terms: "))
num_terms = 1
# convert angle to radians
angle_r = math.radians(angle)
#Calculate actual value of sin(x)
act_val = math.sin(angle_r)


# math maybe a loop
err = 100
while err > 1e-40:
    guess_val = 0
    for n in range(num_terms):
        num1 = (-1)**n
        den1 = math.factorial(2*n +1)
        term1 = math.pow(angle_r, 2*n +1)
        guess_val = guess_val + (num1/den1) * term1
    err = abs(act_val - guess_val)
    num_terms += 1
        

    #Output
print (guess_val, act_val, num_terms)





























