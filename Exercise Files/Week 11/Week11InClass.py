#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:09:08 2019

@author: colemanbeggs
"""

import matplotlib.pyplot as plt
import csv
import numpy as np

t = []
x = []
y = []
z = []
dp = []

f = open('paradata.csv', 'r')
graph = open('DataGraph.txt', 'a')
f_read = csv.reader(f)
next(f_read)

for row in f_read :
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

plt.subplot(2, 1, 2)
plt.plot(t, x, 'b-.', label = 'Gx')
plt.plot(t, y, 'g-', label = 'Gy')
plt.plot(t, z, 'r--', label = 'Gz')
plt.axis([90, 120, -0.2, 0.2])
plt.xlabel('time (s)')
plt.ylabel('Acc. (g)')
plt.legend(loc='lower left', shadow=True, prop={'size': 7.5})
plt.grid()

#graph.append(plt.subplot(2, 1, 1))
#graph.append(plt.subplot(2, 1, 2))

graph.close()
f.close()