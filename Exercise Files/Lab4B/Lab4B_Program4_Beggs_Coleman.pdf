#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:16:37 2019

@author: colemanbeggs
"""

#Machine Producing Widgets
#day = days in production
#wp = widgets produced
#wt = widgets in total

day = int(input("Input a day: ", ))

if 1 <= day <= 10:
    wp = 10
elif 11 <= day <= 60:
    wp = 40
elif 61 <= day <= 100:
    wp = 40 - (day - 60)
elif day > 100:
    wp = 0

if 1 <= day <= 10:
    wt = wp * day
elif 11 <= day <= 60:
    wt = 100 + (wp * (day - 10))
elif 61 <= day <= 100:
    newDay = day - 60
    n = day - 61
    wt = 2100 + (newDay * (39 + wp) / 2)
elif day > 100:
    wt = 2880

print (day, "Days in operation")
print ("Total widgets:", wt)
