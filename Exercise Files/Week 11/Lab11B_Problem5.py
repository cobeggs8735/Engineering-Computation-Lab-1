#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:48:55 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 11b #5
# Date: 4 April 2019

import matplotlib.pyplot as plt

with open('height.out', 'r') as height_out:
    #height = height_out.read()
    heightList = height_out.readlines()
    for i in range(len(heightList)):
        heightList[i] = float(heightList[i])
    
    plt.hist(heightList)
    plt.xlabel("Height")
    plt.ylabel("Height Frequency")
    plt.title("Height vs. Height Frequency")
    #plt.legend(loc = 'upper right', prop = {'size': 20})
    arrow_properties = {
    'facecolor': 'black',
    'shrink': 0.1,
    'headlength': 10,
    'width': 2}
    plt.annotate("Most probable data", (111.0, 2990.0), arrowprops = arrow_properties)