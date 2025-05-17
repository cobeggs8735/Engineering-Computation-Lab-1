#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:08:38 2019

@author: colemanbeggs
"""

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


























