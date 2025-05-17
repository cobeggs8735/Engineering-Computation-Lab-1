#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:59:20 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 11b #2`
# Date: 4 April 2019

import numpy as np

def solution(coefficient, vector):
    import numpy as np
    x = np.linalg.solve(coefficient, vector)
    return x

coefficient_matrix = np.array(np.mat(input("Enter the coefficient matrix (for ex. [1, 2], [2, 1] as '1 2; 2 1'): ")))
solution_vector = np.array(np.mat(input("Enter the solution vector (for ex. [1, 2], [2, 1] as '1 2; 2 1'): ")))

print (solution(coefficient_matrix, solution_vector))
#print (coefficient_matrix)