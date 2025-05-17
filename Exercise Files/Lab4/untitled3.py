#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:14:11 2019

@author: colemanbeggs
"""

string = (input("input a string: ", ))
stringReversed = (string)[::-1]

print (stringReversed)

if string == stringReversed:
    print ("Is this a palindrome?   Yes")
else:
    print ("Is this a palindrome?   No")