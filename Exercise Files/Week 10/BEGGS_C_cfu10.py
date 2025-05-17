#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:29:30 2019

@author: colemanbeggs
"""

import numpy as np
import matplotlib as plt
# Open the file and close it
# Read the file
with open('December_Temp.txt', 'r') as DecemberTemps:
    # Use Readlines to make a list of rows
    r1 = DecemberTemps.readline()
    r2 = DecemberTemps.readline()
    r3 = DecemberTemps.read().replace('\t', ' ').replace('\n',' ')
    #r4 = r3.readlines()
    # Append certain elements of the rows to lists
    cities = [] #Cities list
    days = [] #Days list
    # different list of temps for each city
    # use cities list as lables for temps
    # yaxis label = temps
    # x axis label = days
    tokyo = []
    sydney = []
    houston = []
    elPaso = []
    stockholm = []
    list1 = []
    for i in DecemberTemps.read():
        list1.append(DecemberTemps.readline())

    #plt.grid(True)
    #p1 = plt.plot(days, tokyo, 'b-')
    #p1.legend('Tokyo')
    #p2 = plt.plot(days, sydney, 'r-')
    #p2.legend('Sydney')
    #p3 = plt.plot(days, houston, 'g-')
    #p3.legend('Houston')
    #p4 = plt.plot(days, elPaso, 'c-')
    #p4.legend('El Paso')
    #p5 = plt.plot(days, stockholm, 'm-')
    #p5.legend('Stockholm')
    #plt.xlabel(Days)
    #plt.ylabel(Temps)          
    #plt.show      
    print(r3)