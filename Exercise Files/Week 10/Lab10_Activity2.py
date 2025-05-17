#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:13:17 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: ColemanBeggs
# Section: ENGR102-509
# Assignment: Lab 10 - 2
# Date: 30 March 1019

import matplotlib.pyplot as plt
import numpy as np

values = np.arange(0., 5., 0.2)
plt.plot(values, values, 'r-', values, values**2, 'b-')
plt.show()

def f(t):
    return (np.power(t, 2) + t)

plt.figure(1)
plt.subplot(211)
plt.plot(values, f(values), 'g^')
plt.show()



































