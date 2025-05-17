#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:52:37 2019

@author: colemanbeggs
"""
# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Coleman Beggs
#        Cody Knight
#        Andrew Pool
#        Andrew Mitchell
# Section: ENGR102-509
# Assignment: Semester Project
# Date: 27 April 2019
import math
import re
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
# 1 b
def engr102_plot_data(var_names, data):
    labels = var_names # Copy of the list of variable names
    data_array = np.array(data)
    # Plots a histogram if the data only has one column
    if data_array.shape == (len(data_array),1):
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
# 1 c
def engr102_interpolate_data(var_choices, data):
    n = 1
    data_array = np.array(data) # Creates an array of data
    #Displays options for dependent variable
    for i in range(2,len(var_choices),2):
        print ('%d.' %n, var_choices[i]+' '+var_choices[i+1])
        n += 1
    #Independent variable values array
    ind_vals = data_array[:,0]
    #Inputs
    #Choice for dependent variable
    dep_var = int(input("Select a number for a dependent variable from list provided: "))
    #Array of values for dependent variable
    dep_vals = data_array[:, dep_var] 
    #Query value
    query = float(input("Select a number in range [%f, %f] to interpolate: " %(ind_vals[0],ind_vals[-1])))   
    #Iterates over values then linearly interpolates to get the dependent for independent query
    for x in range(1,len(dep_vals)):
        f = dep_vals[x-1]
        g = dep_vals[x]
        if ind_vals[x-1] <= query <= ind_vals[x]:
            m = (g-f)/(ind_vals[x]-ind_vals[x-1])
            z = m*(query - ind_vals[x]) + dep_vals[x]    
            return z
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
# Handle Text Files
# 3 a
def engr102_word_count(file_name, string_count):
    text = open(file_name, 'r')
    text = str(text.read())
    word_list = re.findall(r'\w+', text)
    counts = []
    tot = 0
    for i in string_count:
        n = 0
        for j in word_list :
            if i == j :
                	n += 1
        counts.append(n)
    for k in word_list :
    	tot += 1    
    return counts, tot
# 3 b
def engr102_string_find(file, search):
    #All lower case search
    search = search.lower()
    #Initial occurrences
    occur = 0
    #Line numbers list
    lines = []
    filelines = file.readlines()
    if len(search) >= 1:
        for i in range(len(filelines)):
            fileline = filelines[i]
            #Searches all lower case seach in all lower case fileline
            if search in fileline.lower():
                # Adds 1 to the number of occurrences
                occur += 1
                # Apends line number to list 'lines'
                lines.append(i+1) #Apends line number to list 'lines'
            else:
                continue
    return occur, lines
# 3 c
def engr102_nuclear_results(text_file_name):
    with open(text_file_name, 'r') as f:   #opens text file to read file names from it
        file_names = []
        for row in f:
            file_names.append(row.rstrip('\n'))    
    #loop to open files and find values for each file and add to list
    diam_rawdata = []
    pitch_rawdata = []
    fact_raw = []    
    for i in file_names: 
        with open(i, 'r')as xfile:
            each_file = xfile.readlines()
            diam_test = 'AVERAGE FUEL ROD DIAM.'
            pitch_test = 'FUEL PIN PITCH'
            fact_test = 'K-INF:'
            for rows in each_file:
                if diam_test in rows:#find fuel diameter line using cm 205
                    diam_rawdata.append(rows[44:54])
                if pitch_test in rows:#found in line (cm) 206
                    pitch_rawdata.append(rows[44:54])
                if fact_test in rows:#find multiplication factor line?
                    fact_raw.append(rows[11:19])    
    #converts raw data (lists of strings to lists of floats)
    pitch_data = [float(i) for i in pitch_rawdata]
    diam_data = [float(i) for i in diam_rawdata]
    factor_data = [float(i) for i in fact_raw]    
    mult_factor = np.array(factor_data)    
    Pitch = np.array(pitch_data)
    Diam = np.array(diam_data)    
    area_fuel = math.pi*np.power(Diam,2)
    area_Moderator = 4*np.power(Pitch,2) - area_fuel
    fuel_ratio = area_Moderator/area_fuel  #calculate moderator to fuel ratio    
    #return moderator to fuel ratio in 2d array
    #return multiplication factor in 2d array
    return_arg = np.array([fuel_ratio, mult_factor])           
    #make plot
    plt.title('Multiplication Factor vs. Moderator to Fuel Ratio')
    plt.plot(fuel_ratio,mult_factor,'r-.')
    plt.xlabel('Moderator to Fuel Ratio')
    plt.ylabel('Multiplication Factor')
    plt.axis([0, 20, 1, 1.5])
    plt.xticks(np.arange(2, 22, step = 2))
    plt.yticks(np.arange(1, 1.55, step = 0.05))    
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':', linewidth='0.05', color='black')
    plt.grid()
    plt.savefig("mod-to-fuel_vs_k.png")
    plt.show()    
    return return_arg
        