#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:25:45 2019

@author: colemanbeggs
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Coleman Beggs
# Section: ENGR102-509
# Assignment: Lab 11b #6 b
# Date: 4 April 2019

def net_profit(names, costs, values):
    if len(names) == len(costs) == len(values):
        profit = {}
        for i in range(len(names)):
            profit.update({values[i] - costs[i] : names[i]})
        profit_keys = list(profit.keys())
        profit_keys.sort()
        return profit.get(profit_keys[0], 'N/A') #profit_keys[0]

# Define three lists
facility_names = ['VEX EDR', 'VEX Pro', 'VEX IQ']
facility_operation_cost = [100.0, 250.0, 200.0]
facility_product_value = [200.0, 300.0, 400.0]

print("Least profitable facility is:", net_profit(facility_names, facility_operation_cost, facility_product_value))