#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:56:55 2019

@author: colemanbeggs
"""

import math

energyBTU = float(input("Input an energy value in BTUs: ")) #British Thermal Units

energyJoules = energyBTU * 1055.06 #Joules

print (energyBTU, "BTUs =", energyJoules, "in Joules")