#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:51:38 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 11b #1`
# Date: 4 April 2019

def primes(n):
    primeFactors = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primeFactors.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primeFactors.append(n)
    return primeFactors

my_factor = int(input("Enter an integer to get the prime factorization: "))

    
if type(my_factor) == int:
    print(primes(my_factor))