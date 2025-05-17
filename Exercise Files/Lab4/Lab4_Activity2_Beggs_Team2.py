#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:23:06 2019

@author: colemanbeggs
"""

print ()

#Part a Evaluating Booleans

a = False
b = True
c = False

if a and b and c:
    print ("a and b and c: True")
else:
    print("a and b and c: False")
    
if a or b or c:
    print ("a or b or c: True")
else:
    print("a or b or c: False")
    
if (not(a and not b)or(not c and b))and(not b)or(not a and b and not c)or(a and not b):
    print ("(not(a and not b)or(not c and b))and(not b)or(not a and b and not c)or(a and not b): True")
else:
    print("(not(a and not b)or(not c and b))and(not b)or(not a and b and not c)or(a and not b): False")
    
if (not((b or not c)and(not a or not c)))or(not(c or not(b and c)))or(a and not c)and(not a or(a and b and c) or (a and ((b and not c) or (not b)))):
    print ("(not((b or not c)and(not a or not c)))or(not(cor not(b an dc)))or(a and not c)and(not a or(a and b and c) or (a and ((b and not c) or (not b)))): True")
else:
    print("(not((b or not c)and(not a or not c)))or(not(c or not(b and c)))or(a and not c)and(not a or(a and b and c) or (a and ((b and not c) or (not b)))): False")

#Part b Writing Boolean expressions

#Is true if just one of a or b is true,but not if both are true or both or false
    
if a and b:
    print ("a and b: False")
elif a or b:
    print ("a or b: True")
else:
    print ("a and b: False")
    
"""
(a) (Note:thisisalsocalledan“exclusiveor”betweenaandb.)
6) Is true if an odd number (i.e. exactly 1 or 3) of the variables a, b, and c is true, and is false otherwise.
"""

#Part c Simplifying Booleans

if (not (a) and (not (b)) or (not (a)) or (a)):
    print ("(not (a) and (not (b)) or (not (a)) or (a)): True")
else:
    print ("(not (a) and (not (b)) or (not (a)) or (a)): False")
    
if (not b and not a) and (not a):
    print ("(not b and not a) and (not a): True")
else:
    print ("(not b and not a) and (not a):False")
