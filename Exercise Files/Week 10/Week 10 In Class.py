#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:26:58 2019

@author: colemanbeggs
"""

import numpy as np
import matplotlib as plt

# 1 
"""
Write a Python program utilizing numpy to find the set difference of two arrays. The set difference will return the sorted, 
unique values in array1 that are not in array2.
Expected Input:
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70, 90] Expected Output:
Set difference between two arrays: [ 0 20 60 80].
"""
import numpy
array1 = [0, 10, 20, 40, 60, 80]
array2 = [10, 30, 40, 50, 70, 90]
print (numpy.setdiff1d(array1, array2))

# 2
'''
Write a Python program utilizing numpy to find the indices of the maximum and minimum values along the given axis of an 
array. Go to the editor
Original array:
array([[ 10, 9, 0, 13, 2],
[ 5, 3, 7, 8, 1],
[10, 11, 12, 13, 14]])
Expected Output:
The Maximum Value of 14 is located on row 3 column 5 The Minimum Value of 0 is located on row 1 column 3
'''

array = [[ 10, 9, 0, 13, 2], 
          [ 5, 3, 7, 8, 1], 
          [10, 11, 12, 13, 14]]
#array_max = numpy.maximum(array)

minx = 100
maxy = -100
row = 0
column = 0
for i in range(len(array)):
    row += 1
    for j in range(len(array[i])):
        column += 1
        if array[i][j] < (minx):
            minx = array[i][j]
            rowmin = row
            columnmin = column
        if array[i][j] > (maxy):
            maxy = array[i][j]
            rowmax = row
            columnmax = column
    column = 0        

# Output
print ("The Maximum value of", maxy,"is located on row", rowmax, "column", columnmax)
print ("The Minimum value of", minx ,"is located on row", rowmin, "column", columnmin)

# 3 
"""
Write a Python program to count the frequency of a user inputted string in a file. Load file: un.txt
"""

#3 write a program to count the frequency of user inputted str in a file: un.txt

# open file for readin
with open('un.txt', 'r') as un:
    read = un.read() # convert to str
    # strip at whitespace, periods, and commas
    spl = read.rstrip('\n')
    un_spl = spl.replace('(', '')
    un_spl2 = un_spl.replace(')', '')
    un_spl3 = un_spl2.replace('.', ' .')
    un_spl4 = un_spl3.replace(',', ' ,')
    # split into a list
    un_fix = un_spl4.split()
    #define variables
    user_input = input('Enter a word, character, or number: ')
    charac = {user_input: 0}
    freq = {}
    count = 0
    charac[user_input] = count
    # loop over list to check for user input
    for i in un_fix:
        if user_input == i:
            count += 1 # count occurences of user input
            charac[user_input] = count
            freq.update(charac)
        else:
            charac[user_input] = count
            freq.update(charac)
            
print(freq)


# 4
"""
Write a Python program to find common words between two documents. Load file: un.txt doi.txt
"""

#import numpy
import numpy as np    
# open un.txt and doi.txt
with open('un.txt', 'r') as un:
    with open('doi.txt', 'r') as doi:
        read_un = un.read() # convert to str
        read_doi = doi.read()
        # strip new lines and puncuation
        splun = read_un.rstrip('\n')
        spldoi = read_doi.rstrip('\n')
        un_spl = splun.replace('(', '')
        doi_spl = spldoi.replace('.', '')
        un_spl2 = un_spl.replace(')', '')
        doi_spl2 = doi_spl.replace(',', '')
        un_spl3 = un_spl2.replace('.', '')
        doi_spl3 = doi_spl2.replace(':', '')
        un_spl4 = un_spl3.replace(',', '')
        doi_spl4 = doi_spl3.replace(';', '')
        # split into list
        un_fix = un_spl4.split()
        doi_fix = doi_spl4.split()
        # convert to array
        un_array = np.array([un_fix])
        doi_array = np.array([doi_fix])
        # find intersecting words
        common = np.intersect1d(un_array, doi_array)
# output array of common words        
print(common)

# 5
"""
Write a program to plot the temperature data for two different cities loaded from separate files. 
The data is formatted as follows: month day year temp. Your plot should use different color markers for each cities. 
Do not use lines.
Load file: TXHOUSTO.txt MABOSTON.txt
"""

boston = open('MABOSTON.txt', 'r')
houston = open('TXHOUSTO.txt','r')

month = []
day = []
year = []
tempHTX = []
tempBMA = []

for i in boston:
    x = 1
for n in houston:
    x = 1
    
boston.close
houston.close

# 6
"""
Using the data files from above, merge the results into a new data file called cities_temp.txt. 
The data is formatted as follows: month day year tempHouston tempBoston.
"""























