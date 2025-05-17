#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:15:20 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 9B - 4
# Date: 24 March 2019

import csv

weatherDataMac = open('WeatherDataMac.csv', 'r')
weatherData = csv.reader(weatherDataMac)
#weatherDataCopy = open('WeatherDataMacCopy.csv', 'a')
#weatherAppender = csv.writer(weatherDataCopy)

list1 = []
list2 = []

for i in weatherData:
    #print (i)
    if i[0] == '1/1/2015':
        avg_temp = i[2]
        print ("Interesting analysis 1:", end=' ')
        print ("Average temperature on January 1st, 2015 is:", avg_temp, 'ºF')

    #weatherAppender.writerow(i)
    if len(i[2]) == 2:
        if i[0] == '1/1/2015'or'1/2/2015'or'1/3/2015'or'1/3/2015''1/4/2015'or'1/5/2015'or'1/6/2015'or'1/7/2015'or'1/8/2015'or'1/9/2015'or'1/10/2015'or'1/11/2015'or'1/12/2015'or'1/13/2015'or'1/14/2015'or'1/15/2015'or'1/16/2015'or'1/17/2015'or'1/18/2015'or'1/19/2015'or'1/20/2015'or'1/21/2015'or'1/22/2015'or'1/23/2015'or'1/24/2015'or'1/25/2015'or'1/26/2015'or'1/27/2015'or'1/28/2015'or'1/29/2015'or'1/30/2015'or'1/31/2015':
            i[2] = int(i[2])
            list1.append(i[2])
    if len(i[5]) == 2:
        list2.append(i[5])

x = 0
y = 0

for n in range(31):
    x += list1[n]
    y += 1

avg_jan = x / y
print ("Interesting analysis 2:", end=' ')
print ("Average temperature in January 2015 is:", avg_jan, "ºF")

v = 0
z = 0

for h in list2:
    v += int(h)
    z += 1

avg_dew = v / z
print ("Interesting analysis 3:", end=' ')
print ("Average Dew Point for Study is:", avg_dew)

weatherDataMac.close()
#weatherDataCopy.close()