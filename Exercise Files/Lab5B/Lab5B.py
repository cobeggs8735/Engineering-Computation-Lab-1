#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 15:25:51 2019

@author: colemanbeggs
"""

O = 0
A = 0.0125
B = 0.0125
C = 0.06
D = 0.18
E = 0.26

strain = float(input("Input a stress value for structural steel greater than zero: ",))

"""
Test cases:
strain = -1, stress = undefined
strain = 0, stress = 0
strain = 0.01, stress = 36
strain = 0.0125, stress = 45
strain = 0.02, stress = 45.312
strain = 0.06, stress = 47
strain = 0.12, strain = 53.49
strain = 0.18, stress = 60
strain = 0.20, stress = 57.5
strain = 0.26, stress = 50
strain = 0.30, stress = beyond breaking point
"""

#Young's Modulus
if O <= strain <= A:
    stress = 3600 * strain
    print ("Stress is", stress)
#Plastic Region
elif B < strain <= C:
    stress = 42.1 * strain + 44.47
    print ("Stress is", stress)
#Strain Hardening Region
elif C < strain <= D:
    stress = 108.3 * strain + 40.5
    print ("Stress is", stress)
#Necking Region
elif D < strain <= E:
    stress = -125 * strain + 82.5
    print ("Stress is", stress)
#Fracture Point
elif strain == E:
    stres = " at fracture point"
    print ("Stress is", stress)
#Beyond Fracture Point
elif E < strain:
    stress = "beyond breaking point"
    print ("Stress is", stress)
#Error Catching
else:
    stress = "undefined"
    print ("Stress is", stress)
