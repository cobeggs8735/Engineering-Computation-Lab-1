#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:08:38 2019

@author: colemanbeggs
"""

#A = [10, 87, 101, 1, 43, 7, 8, 15, 123, 95, 77, 10]
#B = ['cable', 'engr102', 'Zachry', 'INSTRUCTS', 'in', 'students', 'with the', 'Best']
#C = [[1, 2, 3], 'proton', 'electron', [['A', 'B'],[1, 2, 3, 4], 5, 'cable'], ['a', 'b', 'c', 'd', 'e'], 'f']

"""
i. A[:], A[5], A[3], A[-1], and A[-3]
ii. B[:4], B[4:], B[0:], B[:2], B[1:-1], B[3:-2], and B[:5:-3]
iii. C[0][1], C[3][0][:], C[3][1][:2], C[3][1][:-3], C[:], C[3][1][::-1],
"""

"""
i. Find and print the median and mean of A without using median or mean functions.
ii. Find and print the min and max of A without using min/max functions.
iii. Write a program to sort A in descending order without using the sort function.
iv. Create a new list AA that contains only the odd values of A.
v. Find and print the average number of characters for the elements of B.
vi. Using all of the elements of B, construct and print a sentence.
vii. Sort the elements of C in order of increasing length.
viii. Find and print the letter that occurs most frequently in B.
"""

# i

# sort A into ascending order
# if a indecies are odd, the middle indice
# if a is even things get schwifty

#list_len = len(A)

#if (list_len % 2) == 0:
#    for i in A.sort():
        
#else:
    
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Group Member 1: Brennan Reimer
# Group Member 2: Arianna McCauley 
# Group Member 3: Coleman Beggs
# Group Member 4: Ethan Yu
# Section: 509
# Assignment: Lab7 Activity 3
# Date: 2 March 2019

import math

playerValues = {}

i = 0
s1 = 0

while s1 >= 0:
    s1=float(input('Enter the score of first round (enter a negtive to stop): '))   
    if s1 < 0:
        break
    s2=float(input('Enter the score of second round: '))
    name=str(input('Enter the name of the player: '))
    s_tol=s1+s2
    
    playerValues[name] = s_tol
    
    i += 1

values = list(playerValues.values())
keys = list(playerValues.keys())

for j in range(i):
    for h in range(j):
        if values[h] > values[j]:
            values[h], values[j] = values[j],values[h]
            keys[h] ,keys [j] = keys[j], keys[h]
        
        else:
            values[h], values[j] = values[h],values[j]
            keys[h] ,keys [j] = keys[h], keys[j]

l = 0
if (i % 2) == 0:
    median = (values[math.floor((i / 2) - 1)] + values[math.floor((i / 2) + 1)]) / 2
    
    while values[l] < median:
        print (keys[l], ',', end = ' ')
        l += 1
    print ("Made the cut")
    
    while values[l] >= median:
        print (keys[l], ',', end = ' ')
        l += 1
        if l >= i:
            break
    print ("Didn't make the cut")

elif (i % 2) != 0:
    median = int((i / 2) + 0.5)
    
    while values[l] < median:
        print (keys[l], ',', end=' ')
        l +=1
    print ("Made the cut")
    
    while values[l] >= median:
        print (keys[l], ',', end = ' ')
        l += 1
        if l >= i:
            break
    print ("Didn't make the cut")


























