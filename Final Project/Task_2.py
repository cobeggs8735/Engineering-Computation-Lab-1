#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:05:33 2019

@author: colemanbeggs
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# Evaluating Functions
# 2 a
def engr102_load_function(file_name):
    with open(file_name, 'r') as file:
        equations = [] # Initializes List of equations
        for i in file.readlines():
            n = i.strip('\n') # Removes new line char
            equations.append(n) # Appends equations to the list
        print(equations)
        return equations # Returns equations as strings in list

# 2 b
def engr102_plot_function(equations):
    for n in equations: # Iterates over the equations
        points = [] # Initializes a list of points for an equation
        for x in np.arange(0, 10.0, 0.01):
            points.append(eval(n)) # Evaluates expression of nth indecy of equations
        plt.plot(np.arange(0, 10.0, 0.01), points, label=n)
    #plt.ylim(-27, 100) # Set the y limits of plot
    plt.grid()
    plt.legend(loc='best', prop={'size':7}) # Adds legend of labeled lines
    # Saves plot as a .png file
    return plt.savefig('ENGR102 Project 2b.png')

# 2 c
def engr102_integrate_function(equations, bounds, trapezoids, equation):
    # Area of a trapezoid
    # A = ((a + b)/2) * height
    height = (bounds[1] - bounds[0])/trapezoids
    # f(b) = eval(equations[equation])
    x_vals = np.arange(bounds[0], bounds[1], (bounds[1]-bounds[0])/trapezoids)
    equation -= 1
    integral = 0
    points = []
    for x in x_vals:
        points.append(eval(equations[equation]))
    for n in range(len(points)-1):
        integral += ((points[n]+points[n+1])/2)*height
    return integral
            
equations_list = engr102_load_function('equations.txt')
plots = (engr102_plot_function(equations_list))
bounds = 0, 1
traps = 10
equation = 6
integral = engr102_integrate_function(equations_list, bounds, traps, equation)
print(integral)
