#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:44:00 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 9B - 2
# Date: 24 March 2019

# open the celsius file
with open('Celsius.dat', 'r') as celsiusData:
    # loop through the lines of celsiusData
    for i in celsiusData.readlines():
        celsius = float(i)
        # convert lines from celsius to floats
        # open the farenheit file
        with open('Farenheit.dat', 'a') as farenheitData:
            # do the calculation for farenheit
            farenheit = (9/5) * celsius + 32
            # add the data to farenheit file (one per line)
            farenheitData.write(str(farenheit))
            farenheitData.write('\n')
            #print (farenheit)
        