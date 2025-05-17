#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:35:48 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 9B - 3
# Date: 24 March 2019

import csv

# Ask user for loan
# Ask user for annual interest rate
# Ask user for amount being paid monthly
# Ask for the name of the file to write to
# Add '.csv' to whatever name given

# Open the file as a csv file
# Read the csv file
# Create a row for column names
# create the "zero row (No payment, No interest)
# Deterimine first month
# If loan can be paid, iterate until paid
# If loan cannot be paid, iterate for 30 months

# Calculate amount remaining each month
#   Apply monthly payment, increase loan by 1/12 annual interest
# Write month number, and total interset so far (start with 0 months and 0 interest)
#   If loan can be paid, write out values until loan is zero
#   If loan can't be paid write 30 months of data

loan = float(input("Input an amount of money to be loaned: "))
interest_rate = float(input("Input an annual interest rate to be applied (ie 2% would be '.02'): "))
interest = loan * interest_rate
paid = float(input("Input a monthly payment: "))
filename = input("Input a file name for data: ")
filename = filename + '.csv'

with open(filename, 'a') as csvfile:
    row = csv.writer(csvfile)
    new_row = ['Months', 'Interest Accrued', 'Loan Remaining']
    row.writerow(new_row)    
    
    month = 0
    total_interest = 0
    remaining = loan
    new_row = [month, total_interest, remaining]
    row.writerow(new_row)

    remaining = (loan - paid) + (interest / 12) #amount remaining on loan
    
    while remaining < loan:
        loan = remaining
        remaining = (loan - paid) + (interest / 12) #amount remaining on loan
        month += 1
        if remaining <= 0:
            remaining = 0
            new_row = [month, total_interest, remaining]
            row.writerow(new_row)
            break
        total_interest += interest / 12
        new_row = [month, total_interest, remaining]
        row.writerow(new_row)
        
    if remaining >= loan:
        for m in range(1,31):
            month = m
            loan = remaining
            remaining = (loan - paid) + (interest / 12) #amount remaining on loan
            total_interest += interest / 12
            new_row = [month, total_interest, remaining]
            row.writerow(new_row)


            
            
            
            

