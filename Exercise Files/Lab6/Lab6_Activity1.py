# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Thu Feb 21 14:18:28 2019

@author: colemanbeggs
"""

A = 2 #float(input('Enter A in Ax^3 + Bx^2 + Cx + D: '))
B = -6 #float(input('Enter B in Ax^3 + Bx^2 + Cx + D: '))
C = 3 #float(input('Enter C in Ax^3 + Bx^2 + Cx + D: '))
D = -4 #float(input('Enter D in Ax^3 + Bx^2 + Cx + D: '))

tol = 1

a = 2 #float(input('type the first bound'))
b = 3 #float(input('type the second bound'))

Iterations = 0

def f(x):
    return (A*(x**3) + B*(x**2) + C*(x) + D)
p = (a + b)/2

#print(f(a))
while tol > 1e-6:
    if f(p) > 0:
        tol = abs(f(p))
        Iterations += 1
        p = (p+a)/2
    elif f(p) < 0:
        tol = abs(f(p))
        Iterations += 1
        p = (b+p)/2
print(f(p), Iterations)

#test case:A=2,B=-6,C=3,D=-4, a=2,b=3, output:2.719
#test case: A=5,B=3,C=2,D=-3, a=0,b=1, output: 0.349
#test case:A=-⅜, B=-2,C=-1,D=3,a=-3,b=-1,output:-2
#test case:A:9,B=2,C=0,D=-4,a=0,b=1,output:0.696




























