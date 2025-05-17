#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:02:24 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: 509
# Assignment: Lab7B Program 3
# Date: 02 March 2019

# Use Dictionaries
# user inputs a username and a password

pairs = int(input("Enter a number of username and passwords pairs: "))
#username =
#password = 
key = {'john':'nonagon', 'james':'team dye', 'kevin':'coach'}

for i in range(pairs):
    username = input ("Enter a username: ")
    password = input ("Enter a password: ")
    key[username] = password

username = input("Enter a username: ")
password = input("Enter a password: ")

x = 0
while x < 1:
    if key[username] == password:
        print ("Access granted")
        break
    else:
        print ("Enter a valid username and password")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
