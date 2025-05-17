#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:46:15 2019

@author: colemanbeggs
"""
#Converting from Farenheit
#Converting from Celsius
temp = float(input('type the number of the temperature:',))
Scalefrom = str(input('type the scale of temperature:',))
Scaleto = str(input('type the scale desired:',))

if Scalefrom == 'Celsius' and Scaleto == 'Fahrenheit':
    farenheit = (temp*(9/5)+32)
    print('the temp in fahrenheit is', farenheit)
elif Scalefrom == 'Celsius' and Scaleto == 'Kelvin':
    Kelvin = temp + 273
    print('the temp in kelvin is', Kelvin)
elif Scalefrom == 'Celsius' and Scaleto == 'Rankine':
    rankine = (temp*(9/5)+491.67)
    print('the temp in rankine is', rankine)
elif Scalefrom == 'Celsius' and Scaleto == 'Reumer':
    reumer = temp*(4/5)
    print('the temp in reumer is', reumer)
    
#Converting from Farenheit

if (Scalefrom == 'Farenheit') and (Scaleto == 'Celsius'):
    celsius = (temp - 32) * (5 / 9)
    print ("the temp in Celsius is", celsius)
elif (Scalefrom == 'Farenheit') and (Scaleto == 'Kelvin'):
    celsius = (temp - 32) * (5 / 9)
    kelvin = celsius + 273
    print ("temperature in kelvin is", kelvin)
elif (Scalefrom == 'farenheit') and (Scaleto == 'Rankine'):
    celsius = (temp - 32) * (5 / 9)
    rankine = (celsius * (9/5) + 491.67)
    print ('the temp in rankine is', rankine)
elif (Scalefrom == 'farenheit') and (Scaleto == 'Reumer'):
    celsius = (temp - 32) * (5 / 9)
    reumer = celsius * (4/5)
    print ("the temp in reumer is", reumer)