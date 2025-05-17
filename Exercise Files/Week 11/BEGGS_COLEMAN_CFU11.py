#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:09:08 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: CFU 11
# Date: 4 April 2019

import matplotlib.pyplot as plt
import csv
import numpy as np

t = []
x = []
y = []
z = []
dp = []

f = open('paradata.csv', 'r')
graph = open('DataGraph.pdf', 'a')
f_read = csv.reader(f)
next(f_read)

for row in f_read:
    t.append(float(row[0]))
    x.append(float(row[1]))
    y.append(float(row[2]))
    z.append(float(row[3]))
    dp.append(float(row[4]))

plt.subplot(2, 1, 1)
plt.plot(t, x, 'b-.', label = 'Gx')
plt.plot(t, y, 'g-', label = 'Gy')
plt.plot(t, z, 'r--', label = 'Gz')
plt.xlabel('time (s)')
plt.ylabel('Acc. (g)')
plt.axis([0, 850, -0.25, 1.8])
plt.yticks(np. arange(0, 2, step = 0.25))
plt.grid()
plt.subplots_adjust(hspace = .5)
plt.savefig('DataGraph.pdf')

plt.subplot(2, 1, 2)
plt.plot(t, x, 'b-.', label = 'Gx')
plt.plot(t, y, 'g-', label = 'Gy')
plt.plot(t, z, 'r--', label = 'Gz')
plt.axis([90, 120, -0.2, 0.2])
plt.xlabel('time (s)')
plt.ylabel('Acc. (g)')
plt.yticks(np.arange(-0.2, 0.2, step = 0.05))
plt.legend(loc='lower left', prop={'size': 9})
plt.grid()
plt.savefig('DataGraph.pdf')

graph.close()
f.close()