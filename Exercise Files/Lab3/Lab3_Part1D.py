#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:04:33 2019

@author: colemanbeggs
"""

import math

sec_rev = float(input("Input a value of seconds per revolution: "))
hertz = sec_rev * 2 * math.pi

print (sec_rev, "seconds per revolution =", hertz, "Hertz")