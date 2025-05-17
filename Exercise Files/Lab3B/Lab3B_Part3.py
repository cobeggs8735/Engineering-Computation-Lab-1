#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 06:33:49 2019

@author: colemanbeggs
"""

"""
Convert the program from Activity 2 to a function. I have provided the function definition statement and the return statement.
def polygon_calc(num_sides,side_length):
#insert your code here
return Area_polygon, angle_polygon, Dia_circle_I, Dia_circle_C
"""

import math

"""ACI, ACO = polygon_cal(4,1)
print("Area of circle outside",ACO)
print("Area of circle inside",ACI)"""

def polygon_cal(numSides, lenSide):
    
    # Polygon
    
    numSides = int(input("Input a number of  sides of a polygon (atleast 3 sides): ")) #Polygon's sides
    print (numSides, "sided polygon")
    
    lenSide = float(input("Input a side length of a polygon: ")) #Side length of polygon
    print ("Side length =", lenSide)
    
    angPolygon = (numSides - 2) * 180 / numSides #Angle between sides in degrees
    
    p = lenSide * numSides #Perimeter of polygon
    a = lenSide / (2 * math.tan(math.radians(180 / numSides))) #Apothem value
    areaPolygon = (a * p) / 2
    
    # Circle inside polygon
    
    diamCircleInside = 2 * a #Diameter of circle inside polyogn
    radiusInside = a #Radius of circle inside polygon
    areaCircleInside = math.pi * radiusInside**2 #Area of circle inside polygon (πr**2)
    
    # Circle outside polygon
    
    radiusOutside = a / (math.sin(math.radians(angPolygon / 2))) #Radius of circle outside polygon
    diamCircleOutside = 2 * radiusOutside
    areaCircleOutside = math.pi * radiusOutside**2 #Area of circle outsie polygon (πr**2)
    
    print ()
    print (numSides, "sided polygon")
    print ("Side length =", lenSide)
    print (angPolygon, "degrees between sides")
    print ("Perimeter =", p)
    print ("Apothem =", a)
    print ("Area of polygon =", areaPolygon)
    print ()
    print ("Diameter of circle inside polygon:", diamCircleInside)
    print ("Area of circle inside polygon:", areaCircleInside)
    print ()
    print ("Radius of circle outside polygon =", radiusOutside)
    print ("Area of circle outside polygon =", areaCircleOutside)
    #ACI, ACO = polygon_cal(4, 1)
    #print ("Area of circle outside", ACO)
    #print ("Area of circle inside", ACI)
    #return (areaPolygon, angPolygon, diamCircleInside, diamCircleOutside)
    #return (areaCircleInside, areaCircleOutside)
    return (areaCircleInside, areaCircleOutside)

areaCircleInside, areaCircleOutside = polygon_cal (4,1)
print (polygon_cal)
