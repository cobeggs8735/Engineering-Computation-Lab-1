#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:16:33 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 11b #6 c
# Date: 4 April 2019

def avg_velocity(time, distance):
    if len(time) == len(distance):
        avg_velocities = []
        for i in range(len(time) - 1):
            velocity = (distance[i + 1] - distance[1]) / (time[i + 1] - time[i])
            avg_velocities.append(velocity)
        return avg_velocities
    else:
        return "Invalid time and distance inputs"

time = [1, 2, 3, 4, 5]
distance = [1, 2, 3, 4, 5]
print (avg_velocity(time, distance))