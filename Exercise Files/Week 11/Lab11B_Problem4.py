#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:48:33 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 11b #4
# Date: 4 April 2019

import matplotlib.pyplot as plt

time = []
Al28 = []
Al29 = []

with open('Number 4 Graph.png', 'a') as graph:

    with open('Al_decay.txt', 'r') as Al_decay:
        Al_decay.readline
        values_list = Al_decay.readlines()
        for i in range(len(values_list)):
            k = values_list[i]
            x = k.split('\t')
            if i > 0:
                time.append(float(x[0]))
                Al28.append(float(x[1]))
                Al29.append(float(x[2]))
                
        plt.plot(time, Al28, 'b--', label = 'Al28')
        plt.plot(time, Al29, 'g-.', label = 'Al29')
        plt.xlabel('Time (s)')
        plt.ylabel('Counts')
        plt.title('Al28 and Al29 Isotopes Decay')
        plt.legend(shadow = True, loc = 'upper right', prop = {'size': 15})
        plt.savefig('Number 4 Graph.png')