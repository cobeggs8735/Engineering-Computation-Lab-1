#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:59:59 2019

@author: colemanbeggs
"""

# Activity one
with open('doi.txt.rtf', 'r') as doitxt:
    join = ' '
    doi = doitxt.read()
    new = doi.replace('\n', ' ')
    #new = join.join(new)
    new = new.replace(':', ' ')
    #new = join.join(new)
    new = new.replace('.', ' ')
    #new = join.join(new)
    new = new.replace(';', ' ')
    #new = join.join(new)
    new = new.replace(',', ' ')
    new = new.replace('  ', ' ')
    #new = join.join(new)
    #new = new.split('-')
    #new = join.join(new)
    #new = new.split('\')
    #new = join.join(new)
    new = new.split(' ')
    #print (new)
    short = 'supercalifragilistic'
    long = 'a'
    for i in new:
        if len(i) < len(short):
            short = i
        if len(i) > len(long):
            long = i
            
    #print (short)
    #print (long)
    
    dic = {}
    for n in range(len(new)):
        x = 0
        for j in range(len(new)):
            if str(new[j]) == str(new[n]):
                x += 1
                dic.update({str(new[j]) : x})
    print (dic)       
        
# Activity two

