#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:59:58 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: 509
# Assignment: Lab7B Program 2
# Date: 02 March 2019

#Vector Math

#Define Vector A
A = []
a = 0
while a != 1e9:
    a = float(input("Enter a vector component for A (enter 1e9 to stop): "))
    if a == 1e9:
        break
    A.append(a)

#Define Vector B 
B = []
b = 0
while b != 1e9:
    b = float(input("Enter a vector component for B (enter 1e9 to stop): "))
    if b == 1e9:
        break
    B.append(b)

added = []
difference = []
dotProd = 0

for i in range(len(A)):
    added.append(A[i] + B[i])
    difference.append(A[i] - B[i])
    #dot product is A[0]*B[0] + A[1]*B[1]
    dotProd += A[i] * B[i]

print ("A =", A)
print ("B =", B)
print ("A + B =", added)
print ("A - B =", difference)
print ("Dot Product =", dotProd)
