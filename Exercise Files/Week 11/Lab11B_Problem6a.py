#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:56:09 2019

@author: colemanbeggs
"""
# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 11b #6 a
# Date: 4 April 2019

def box_volume_remaining(length, width, height, hole_radius):
    import math
    box_volume = length * width * height
    hole_volume = math.pow(hole_radius, 2) * math.pi * height
    remaining_volume = box_volume - hole_volume
    return remaining_volume

length = 5#float(input("Enter a length for a box: "))
width = 6#float(input("Enter a width for a box: "))
height = 7#float(input("Enter a height for a box: "))
hole_radius = 1#float(input("Enter the radius of a hole to be drilled: "))

print ("Remaining volume is:", box_volume_remaining(length, width, height, hole_radius))