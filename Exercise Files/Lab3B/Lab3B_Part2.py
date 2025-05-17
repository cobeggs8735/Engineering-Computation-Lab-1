#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 06:33:15 2019

@author: colemanbeggs
"""

"""
Calculate:
The area of a polygon
The interior angle of a polygon
The diameter of a circle inscribed within the polygon
The diameter of a circle circumscribed outside the polygon
"""

"""
The formula for calculating the length of the apothem is this: 
the length of the side (s) divided by 2 times the tangent (tan) of 180 degrees divided by the number of sides (n)
"""
import math
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

diamInside = 2 * a #Diameter of circle inside polyogn
radiusInside = a #Radius of circle inside polygon
areaCircleInside = math.pi * a**2 #Area of circle inside polygon (πr**2)

# Circle outside polygon

radiusOutside = a / (math.sin(math.radians(angPolygon / 2))) #Radius of circle outside polygon
areaCircleOutside = math.pi * radiusOutside**2 #Area of circle outsie polygon (πr**2)

print ()
print (numSides, "sided polygon")
print ("Side length =", lenSide)
print (angPolygon, "degrees between sides")
print ("Perimeter =", p)
print ("Apothem =", a)
print ("Area of polygon =", areaPolygon)
print ()
print ("Diameter of circle inside polygon:", diamInside)
print ("Area of circle inside polygon:", areaCircleInside)
print ()
print ("Radius of circle outside polygon =", radiusOutside)
print ("Area of circle outside polygon =", areaCircleOutside)
