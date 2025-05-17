#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:08:44 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 11b #3 a - f`
# Date: 4 April 2019

# Problem 3
import numpy as np

def solution(coefficient, vector):
    import numpy as np
    x = np.linalg.solve(coefficient, vector)
    return x

# Problem 3 a
    
coefficientMatrix_a = np.array(np.mat('1 1; 1 -1'))
solutionVector_a = np.array(np.mat('4; 2'))

solutions_a = 'Solutions for 3a are:', solution(coefficientMatrix_a, solutionVector_a)
print (solutions_a)
    
# Problem 3 b

coefficientMatrix_b = np.array(np.mat('3 2; 5 -2'))
solutionVector_b = np.array(np.mat('4; 12'))

solutions_b = 'Solutions for 3b are:', solution(coefficientMatrix_b, solutionVector_b)
print(solutions_b)
    
# Problem 3 c

coefficientMatrix_c = np.array(np.mat('1 -2 3; -1 3 0; 2 -5 5'))
solutionVector_c = np.array(np.mat('9; -4; 17'))

solutions_c = 'Solutions for 3c are:', solution(coefficientMatrix_c, solutionVector_c)
print(solutions_c)
    
# Problem 3 d

coefficientMatrix_d = np.array(np.mat('6 -1 1; 4 0 -3; 0 2 5 '))
solutionVector_d = np.array(np.mat('-1; -19; 25'))

solutions_d = 'Solutions for 3d are:', solution(coefficientMatrix_d, solutionVector_d)
print(solutions_d)
    
#Problem 3 e 

coefficientMatrix_e = np.array(np.mat('1 0 1; 2 0 1; 2 1 0'))
solutionVector_e = np.array(np.mat('12; 15; 26'))

solutions_e = 'Solutions for 3e are:', solution(coefficientMatrix_e, solutionVector_e)
print(solutions_e)
    
#Problem 3 f

coefficientMatrix_f = np.array(np.mat('1 -1 1; 3 -2 0; 0 2 4'))
solutionVector_f = np.array(np.mat('0; 7; 8'))

solutions_f = 'Solutions for 3f are:', solution(coefficientMatrix_f, solutionVector_f)
print(solutions_f)

solution_pdf = open('Number 3 Solutions.txt', 'w')
solution_pdf.write(str(solutions_a))
solution_pdf.write('\n')
solution_pdf.write(str(solutions_b))
solution_pdf.write('\n')
solution_pdf.write(str(solutions_c))
solution_pdf.write('\n')
solution_pdf.write(str(solutions_d))
solution_pdf.write('\n')
solution_pdf.write(str(solutions_e))
solution_pdf.write('\n')
solution_pdf.write(str(solutions_f))
solution_pdf.write('\n')
solution_pdf.close()