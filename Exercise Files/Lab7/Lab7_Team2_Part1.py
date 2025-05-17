#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:31:06 2019

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
# Assignment: Lab7 Activity 1
# Date: 2 March 2019
#Creating list of productions, need an empty list, then use a while loop so user can enter as #many days as they want to

widgets = []
x = int(input('type how many widgets are produced each day, type a negative when finished:'))

while x >= 0: #condition allows user to enter a negative when they are finished
    widgets.append(x)
    x = int(input('type how many widgets are produced each day, type a negative when finished:'))

increasing_intervals = 0
decreasing_intervals = 0
intrvl = 1 #begin with one day intervals and increment to length of the list minus one

while intrvl < len(widgets): #the interval cannot be larger than or equal to length of list
    for i in widgets[::intrvl]: #iterating using the length of the interval starting at 1
        count = 0 #conditionals adding to the number of increasing or decreasing intervals
        if widgets[count+intrvl] - widgets[count] > 0: 
            increasing_intervals += 1
        elif widgets[count+intrvl] - widgets[count] < 0:
            decreasing_intervals += 1
        count += intrvl
        numintrvl = len(widgets)-1
    numintrvl -= 1 
    percent_increase = (increasing_intervals / numintrvl) * 100 #part/whole * 100
    percent_decrease = (decreasing_intervals / numintrvl) * 100
    intrvl += 1
    print('for', intrvl, 'day intervls', percent_increase, '% were increasing and', percent_decrease, '% were decreasing') #output statement describing data
