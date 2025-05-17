#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:16:35 2019

@author: colemanbeggs
"""
"""
online source
https://formulas.tutorvista.com/physics/reynolds-number-formula.html
If Re < 2000 the flow is Laminar
If Re > 4000 the flow is turbulent
If 2000 < Re < 4000 it is called transition flow
"""

v = float(input("Input a fluid velocity in m/s: ", )) #Velocitym/s
L = float(input("Input a characteristic linear dimension: ", )) #Characteristic linear dimension m
kv = float(input("Input a kinematic viscosity: ", )) #Kinematic Viscosity m^2/s
Re = (v * L) / kv

if Re < 2000:
    flow = "Laminar"
elif Re > 4000:
    flow = "Turbulent"
elif 2000 <= Re <= 4000:
    flow = "Transition Flow"

print ("Velocity =", v, "m/s")
print ("Characteristic Linear Dimension", L, "Meters")
print ("Kinematic Viscosity", kv, "m^2/s")
print ("Reynolds Number", Re)
print ("Flow is:", flow)