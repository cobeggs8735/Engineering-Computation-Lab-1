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

import numpy as np

'''
a = np.arange(15).reshape(3, 5)
print('a =', a)
print('a.shape:', a.shape)
print('a.ndim.name:', a.ndim)
print('a.dtype.name:', a.dtype.name)
print('a.itemsize:', a.itemsize)
print('a.size:', a.size)
print('type(a):', type(a))

b = np.array([6, 7, 8])
print('b =', b)
print('type(b)', type(b))
'''

'''
a = np.array([2, 3, 4])
print(a)
print(a.dtype)

b = np.array([1.5, 3.5, 5.1])
print(b.dtype)

b = np.array([[1.5, 2, 3], 
              [4, 5, 6]])
print(b)

c = np.array([[1, 2], 
              [3, 4]], dtype = complex)
print(c)

print(np.zeros( (3, 4) ))
print(np.ones( (2, 3, 4) ))
print(np.empty( (2, 3) ))
'''

'''
a = np.floor(10*np.random.random((3, 4)))
print(a)
print(a.shape)
print(a.ravel())
print(a.reshape(6, 2))
print(a.T)
print(a.T.shape)
print(a.shape)
print(a)
print(a.resize((2, 6)))
print(a.reshape(3, -1))
'''

'''
a = np.arange(6)
print(a)

b = np.arange(12).reshape(4, 3)
print(b)

c = np.arange(24).reshape(2, 3, 4)
print(c)
'''

'''
a = np.array( [20, 30, 40, 50] )
b = np.arange(4)
print(b)
c = a - b
print(c)
print(b**2)
print(10 * np.sin(a))
print(a < 35)
A = np.array( [[1, 1], 
               [0, 1]] )
B = np.array( [[2, 0], 
               [3, 4]] )
print(A * B)
print(A @ B)
print(A.dot(B))

a = np.ones((2, 3), dtype = int)
b = np.random.random((2, 3))
a *= 3
print(a)
b += a
print(b)
#a += b
a = np.ones(3, dtype = np.int32)
b = np.linspace(0, np.pi, 3)
print(b.dtype.name)
c = a + b
print(c)
d = np.exp(c*1j)
print(d)
print(d.dtype.name)

a = np.random.random((2, 3))
print(a)
print(a.sum())
print(a.min())
print(a.max())
'''




# Part (d)

A = np.array([[1, 2, 3, 4], 
              [4, 3, 2, 1], 
              [2, 3, 1, 4]])
print('A:', A)

B = np.array([[1, 2], 
              [3, 4], 
              [4, 3], 
              [2, 1]])
print('B:', B)

C = np.array([[1, 2, 3], 
              [3, 2, 1]])
print('C:', C)

D = np.array([[1], 
             [2], 
             [3]])
print('D:', D)

E = A @ B @ C
print('E:', E)
print("Transpose of E:", E.transpose())

j = (E * x) / D
print(np.linalg.solve(x, j)) # Maybe right IDK