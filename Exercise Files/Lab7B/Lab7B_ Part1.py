#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:50:24 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: 509
# Assignment: Lab7B Program 1
# Date: 02 March 2019

# Pig Latin 

#User Input a Word

word = str(input("Enter a word (all lower case letters): "))

#Define a pig latin word

while word != 'stop':
    #Define a pig latin word
    
    if (word[0] == 'a') or (word[0]== 'e') or (word[0] == 'i') or (word[0] == 'o') or (word[0] == 'u') or (word[0] == 'y'):
        pig_word = (word + 'yay')
        print (pig_word)
    
    else:
        pig_word = (word[1:] + word[0] + 'yay')
        print (pig_word)
    
    #Enter a new word to be processed
    
    word = str(input("Enter another word (type 'stop' to stop program): "))

print ("Program terminated")    