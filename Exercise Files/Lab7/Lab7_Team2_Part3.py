#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:32:59 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Group Member 1: Brennan Reimer
# Group Member 2: Arianna McCauley 
# Group Member 3: Coleman Beggs
# Group Member 4: Ethan Yu
# Section: 509
# Assignment: Lab7 Activity 3
# Date: 2 March 2019
a = ['R','N','B','Q','K','B','N','R'] #set up 8 lists, one for each row of the board
b = ['P','P','P','P','P','P','P','P']
c = ['*','*','*','*','*','*','*','*']
d  = c
e  = c
f  = c
g = ['p','p','p','p','p','p','p','p']
h = ['r','n','b','q','k','b','n','r']
board = [a,b,c,d,e,f,g,h]
x = 'go' #enter loop to begin playing the game
while x != 'done' : #user enters ‘stop’ when done playing
   for i in board:
        print(i) #prints out board after every move 
   x = input('type row of piece you want to move, type done when done playing:')
   y = int(input('type column of piece you want to move, they are labled 0 to 7 left to right:'))
   q = input('type row of square you want to move to:')
   p = int(input('type column of piece square you want to move to:'))
   #swaps pieces 
   board[q[p]] = board[x[y]]
   board[x[y]] = board[q[p]] 
