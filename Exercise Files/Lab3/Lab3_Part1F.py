#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:28:45 2019

@author: colemanbeggs
"""

farenheit = float(input("Input a value of temperature in farenheit: "))
celsius = (farenheit-32) * (5/9)
print (farenheit, "ºF =", celsius, "ºC")