#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:57:33 2019

@author: colemanbeggs
"""

pressurePascal = float(input("Input a pressure value in Pascals: "))

pressure_Hg = pressurePascal * 0.00750062

print (pressurePascal, "Pascals =", pressure_Hg, "in Millimeters of Hg")