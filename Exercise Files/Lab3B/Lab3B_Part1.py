#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:19:18 2019

@author: colemanbeggs
"""

"""
Calculate angle between two 3D point
3D position of an observer
3D position of first observed point
3D position of secendo observed point
Calculate output in degrees
Read in points from user (x, y, z)
Calculate the two vectors from observed points
Normalize vectors
Calculate dot product of the two vectors
Use dot product to calculate the angle between the two vectors
Output answer in degrees
"""

import math
import numpy

#Point Inputs
x1 = int(input ("Input the 3D x point of the observer: ",)) #Observer x
y1 = int(input ("Input the 3D y point of the observer: ",)) #Observer y
z1 = int(input ("Input the 3D z point of the observer: ",))#Observer z
observer = (x1, y1, z1) #Observer point
x2 = int(input ("Input the 3D x point of the observer: ",)) #Observed x point 1
y2 = int(input ("Input the 3D y point of the observer: ",)) #Observed y point 1
z2 = int(input ("Input the 3D z point of the observer: ",)) #Observed z point 1
observed1 = (x2, y2, z2) #First observed point
x3 = int(input ("Input the 3D x point of the observer: ",)) #Observed x point 2
y3 = int(input ("Input the 3D y point of the observer: ",)) #Observed y point 2
z3 = int(input ("Input the 3D z point of the observer: ",)) #Observed z point 2
observed2 = (x3, y3, z3) #Second observed point
print ()
print ("Observer point:", observer)
print ("First observed point:", observed1)
print ("Second observed point:", observed2)

#Vectors, Vector Magnitude & Dot Product
observedVec1 = (x1 - x2, y1 - y2, z1- z2) #Vector of observer and observed point
observedVec2 = (x1 - x3, y1 - y3, z1- z3) #Vector of two observed points
dotProduct = numpy.dot(observedVec1, observedVec2) #Dot product of two vectors
observerVecLength = numpy.linalg.norm(observedVec1) #Magnitude of observer vector
observedVecLength = numpy.linalg.norm(observedVec2) #Magnitude of observed vector

print ()
print ("Observed vector 1:", observedVec1)
print ("Observed vector 2:", observedVec2)
print ("Dot product of two vectors:", dotProduct)
print ("Observer vector length:", observerVecLength)
print ("Observed vector length:", observedVecLength)

# Angle
angle = math.acos(math.radians(dotProduct / (observerVecLength * observedVecLength))) #Angle between vectors

print ()
print ("Angle between vector in degrees:", angle)
