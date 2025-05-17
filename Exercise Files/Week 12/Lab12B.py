#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:53:03 2019

@author: colemanbeggs
"""

#%gui tk

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 12 B
# Date: 10 April 2019

import turtle
import math

def tally_marker(x): #Function for drawing the tallies
    x = 0
    y = 350
    columns = 0
    
    tallymarks = turtle.Turtle()
    tallymarks.shape("turtle")
    tallymarks.pencolor('blue')
    tallymarks.penup()
    tallymarks.right(90)
    tallymarks.speed(10)
    
    for i in range(1, num_tallies+1):
        if(i%5 == 0): #Draws the diagonal line
            tallymarks.right(135)
            tallymarks.forward(30 * math.sqrt(2))
            tallymarks.right(225)
            columns += 1
            
        elif columns == 5: #Starts a new row of tallies
            x = 0
            y -= 50
            columns = 0
            tallymarks.penup()
            tallymarks.goto(-300, y)
            tallymarks.pendown()
            tallymarks.forward(30)
        
        else: #Draws the vertical lines
            tallymarks.penup()
            tallymarks.goto((x-30)*10, y)
            tallymarks.pendown()
            tallymarks.forward(30)
        x = x + 1
        
        
num_tallies = int(input("Enter a number: ")) #Number of tallies

tally_marker(num_tallies) #Draws the tallies