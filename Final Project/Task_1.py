#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:02:33 2019

@author: colemanbeggs
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# Handle Numeric Data
# 1 a
def engr102_load_data(file_name, delim):
    with open(file_name, 'r') as file:
        # Reads the first line
        var_names = file.readline()
        # Converts first line to list of variable names
        var_names = var_names.strip('\n')
        var_names = var_names.split(delim)
        # Reads second line of file
        var_units = file.readline()
        # Converts line to list of variable units
        var_units = var_units.strip('\n')
        var_units = var_units.split(delim)
        num_vars = str(len(var_names))
        var_names_units = []
        # Makes one list of variable names and units
        for i in range(int(num_vars)):
            var_names_units.append(var_names[i])
            var_names_units.append(var_units[i])
        data = [] # List of data
        for n in file:
            # Makes a list of the line
            n = n.strip('\n')
            n = n.split(delim)
            # Initializes a list of float values for each line
            float_line = []
            for x in n:
                # Converts the string to a float and appends to data
                x = float(x)
                float_line.append(x) # Appends float values to the float line
            data.append(float_line) # Appends the list of floats to the data list
        # Num of varibales string
        if len(var_names) == 1: # One variable
            variables = 'one'
        else: # Multiple variables
            variables = 'multiple'
        return variables, var_names_units, data # Outputs appropriate set of variables

a,b,c = engr102_load_data('trig.dat',' ')

# 1 b
def engr102_plot_data(var_names, data):
    labels = var_names # Copy of the list of variable names
    data_array = np.array(data)
    # Plots a histogram if the data only has one column
    if data_array.shape == (len(data_array), 1):
        plt.hist(data_array)
        plt.ylabel('Frequency')
        plt.xlabel(str(labels[0])+' '+str(labels[1]))
        #plt.axvline(data_array.mean(),color='k', linestyle='dashed', label='Mean')
        #plt.text(data_array.std(), label="Standard Dev")
        mu = round(data_array.mean(), 4)
        sigma = data_array.std()
        textstr = '\n'.join((
            r'$\mu=%.2f$' % (round(mu, 4), ),
            r'$\sigma=%.2f$' % (sigma, )))
        # place a text box in upper left in axes coords
        plt.figtext(0.75, 0.75, textstr)#, fontsize='xx-small')
        return plt.savefig("ENGR102Project1.bHistogram.png") # Saves figure as described
    # Plots all other data
    else:
        n = 1 # Column of data
        for i in range(len(labels)):
            if ((i % 2) == 0)and(i > 0): # Plots the nth column of data
                plt.scatter(data_array[:, 0], data_array[:,n], s=1, label=str(labels[i])+' '+str(labels[i+1]))
                n += 1
            else: # Labels y axis
                plt.xlabel(str(labels[0])+' '+str(labels[1]))# Labels x axis
                plt.ylabel("Dependent Variables") # Labels y axis
        plt.grid()
        plt.legend(loc='best', prop={'size':9}, markerscale=3) # The legend of the plot
        return plt.savefig("ENGR102Project1.bPlot.png") # Saves figure as described

engr102_plot_data(b, c)
    
# 1 c
def engr102_interpolate_data(var_choices, data):
    n = 1
    data_array = np.array(data) # Creates an array of data
    #Displays options for dependent variable
    for i in range(2,len(b),2):
        print ('%d.' %n, b[i]+' '+b[i+1])
        n += 1
    #Independent variable values array
    ind_vals = data_array[:,0]
    #Inputs
    #Choice for dependent variable
    dep_var = int(input("Select an independent variable number from list provided: "))
    #Array of values for dependent variable
    dep_vals = data_array[:, dep_var] 
    #Query value
    query = float(input("Select a number in range [%f, %f] to interpolate: " %(ind_vals[0],ind_vals[-1])))   
    #Iterates over values then linearly interpolates to get the dependent for independent query
    for x in range(1,len(dep_vals)):
        f = dep_vals[x-1]
        g = dep_vals[x]
        if ind_vals[x-1] < query <= ind_vals[x]:
            m = (g-f)/(ind_vals[x]-ind_vals[x-1])
            z = m*(query - ind_vals[x]) + dep_vals[x]    
            return z

z = (engr102_interpolate_data(b, c))
