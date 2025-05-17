#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:04:49 2019

@author: colemanbeggs
"""
import numpy as np
import matplotlib.pyplot as plt

def polynomial(coeffs, x):
    y = []
    for i in range(len(coeffs)):
        y.append(x)
    
    coeffs_array = np.array(coeffs)
    y = np.array(y)
    func = np.power(y, np.arange(len(coeffs))) @ coeffs_array
    
    return func

coef = []
new = 0

#while new != 'done':
#	coef.append(new)
#	new = str(input("Enter coefficients one at a time, enter 'done' when finished : "))
    
#coef.remove(0)

#coef_float = np.array(2, 3, 5)

coef_float = [5, 3, 2]

#coef_float = [float(i) for i in coef]

def derivative(poly1):
  '''
  Uses Power Rule to change variables into derived version
  '''
  der = [0, poly1[0]*3, poly1[1]*2, poly1[2]]
  return der


'''
poly_der1 = derivative(poly)
poly_der2 = derivative(poly_der1)'''

#x = range(-2, 2)#np.linspace(-2, 2, 100, endpoint=True)
#func = polynomial(coef_float, x)
#deriv1 = derivative(func)
#deriv2 = derivative(deriv1)

x = np.arange(-5, 35, (35-(-5))/len(coef_float))
'''
F = p(poly[0], poly[1], poly[2], poly[3], X)
F_der1 = p(poly_der1[0], poly_der1[1], poly_der1[2], poly_der1[3], X)
F_der2 = p(poly_der2[0], poly_der2[1], poly_der2[2], poly_der2[3], X)
'''

#plt.plot( np.polyval(coef_float, x), label="Function")

plt.plot(x, polynomial(coef_float, x),'g-', label='Function')

#plt.plot(x, F_der1, label="F_der")
#plt.plot(x, F_der2, label="F_der2")
plt.legend()
plt.show()
