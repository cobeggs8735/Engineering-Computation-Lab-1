#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:25:40 2019

@author: colemanbeggs
"""

grocery_list = ['carrots', 'yogurt', 'pizza rolls', 'ramen', 'ice cream', 'candy', 'beer']

print(grocery_list[:3])
print(grocery_list)


num_list = [100, 34, 56, 1, 11, 13]
num_list2 = num_list.sort()
print (num_list)
num_list.append(3)
print (num_list)

grocery_list[1] = 'gogurt'
print (grocery_list)

list1 = [grocery_list, 5, 'cable']
print (list1)
print (list1[0][2])