#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:42:59 2019

@author: colemanbeggs
"""

print ()
print ("Coleman Beggs")
print ("ENGR: 102-509")
print ("I'm a world champion robot driver.")

import math
import numpy

# fraction = (t-t1)/(t2-t1)
# x = x1 + fraction * (x2-x1)
# y = y1 + fraction * (y2-y1)
# z = z1 + fraction * (z1-z2)

print ()

t13 = 13 #Time
x13 = 1 #x
y13 = 3 #y
z13 = 7 #z

t84 = 84 #Time
x84 = 23 #z
y84 = -5 #y
z84 = 10 #z

print ("At time 13", "(", x13,",", y13, ",", z13, ")")
print ("At time 84", "(", x84, ",", y84, ",", z84, ")")
print ()

t20 = 20 #time 20
h20 = (t20 - t13) / (t84 - t13) #contsant 20

x20 = x13 + h20 * (x84-x13) # x at time 20
y20 = y13 + h20 * (y84-y13) # y at time 20
z20 = z13 + h20 * (z84-z13) # z at time 20

print ("X at time 20 =", x20)
print ("Y at time 20 =", y20)
print ("Z at time 20 =", z20)
print ("------------------")

t21 = 21 #time 21
h21 = (t21 - t13) / (t84 - t13) #contsant 21

x21 = x13 + h21 * (x84-x13) # x at time 21
y21 = y13 + h21 * (y84-y13) # y at time 21
z21 = z13 + h21 * (z84-z13) # z at time 21

print ("X at time 21 =", x21)
print ("Y at time 21 =", y21)
print ("Z at time 21 =", z21)
print ("------------------")

t22 = 22 #time 22
h22 = (t22 - t13) / (t84 - t13) #contsant 22

x22 = x13 + h22 * (x84-x13) # x at time 22
y22 = y13 + h22 * (y84-y13) # y at time 22
z22 = z13 + h22 * (z84-z13) # z at time 22

print ("X at time 22 =", x22)
print ("Y at time 22 =", y22)
print ("Z at time 22 =", z22)
print ("------------------")

t23 = 23 #time 23
h23 = (t23 - t13) / (t84 - t13) #contsant 23

x23 = x13 + h23 * (x84-x13) # x at time 23
y23 = y13 + h23 * (y84-y13) # y at time 23
z23 = z13 + h23 * (z84-z13) # z at time 23

print ("X at time 23 =", x23)
print ("Y at time 23 =", y23)
print ("Z at time 23 =", z23)
print ("------------------")

t24 = 24 #time 24
h24 = (t24 - t13) / (t84 - t13) #contsant 24

x24 = x13 + h24 * (x84-x13) # x at time 24
y24 = y13 + h24 * (y84-y13) # y at time 24
z24 = z13 + h24 * (z84-z13) # z at time 24

print ("X at time 24 =", x24)
print ("Y at time 24 =", y24)
print ("Z at time 24 =", z24)
print ("------------------")

t25 = 25 #time 25
h25 = (t25 - t13) / (t84 - t13) #contsant 25

x25 = x13 + h25 * (x84-x13) # x at time 25
y25 = y13 + h25 * (y84-y13) # y at time 25
z25 = z13 + h25 * (z84-z13) # z at time 25

print ("X at time 25 =", x25)
print ("Y at time 25 =", y25)
print ("Z at time 25 =", z25)
print ("------------------")

t26 = 26 #time 26
h26 = (t26 - t13) / (t84 - t13) #contsant 26

x26 = x13 + h26 * (x84-x13) # x at time 26
y26 = y13 + h26 * (y84-y13) # y at time 26
z26 = z13 + h26 * (z84-z13) # z at time 26

print ("X at time 26 =", x26)
print ("Y at time 26 =", y26)
print ("Z at time 26 =", z26)
print ("------------------")

t27 = 27 #time 27
h27 = (t27 - t13) / (t84 - t13) #contsant 27

x27 = x13 + h27 * (x84-x13) # x at time 27
y27 = y13 + h27 * (y84-y13) # y at time 27
z27 = z13 + h27 * (z84-z13) # z at time 27

print ("X at time 27 =", x27)
print ("Y at time 27 =", y27)
print ("Z at time 27 =", z27)
print ("------------------")

t28 = 28 #time 28
h28 = (t28 - t13) / (t84 - t13) #contsant 28

x28 = x13 + h28 * (x84-x13) # x at time 28
y28 = y13 + h28 * (y84-y13) # y at time 28
z28 = z13 + h28 * (z84-z13) # z at time 28

print ("X at time 28 =", x28)
print ("Y at time 28 =", y28)
print ("Z at time 28 =", z28)
print ("------------------")

t29 = 29 #time 29
h29 = (t29 - t13) / (t84 - t13) #contsant 29

x29 = x13 + h29 * (x84-x13) # x at time 29
y29 = y13 + h29 * (y84-y13) # y at time 29
z29 = z13 + h29 * (z84-z13) # z at time 29

print ("X at time 29 =", x29)
print ("Y at time 29 =", y29)
print ("Z at time 29 =", z29)
print ("------------------")

t30 = 30 #time 30
h30 = (t30 - t13) / (t84 - t13) #contsant 30

x30 = x13 + h30 * (x84-x13) # x at time 30
y30 = y13 + h30 * (y84-y13) # y at time 30
z30 = z13 + h30 * (z84-z13) # z at time 30

print ("X at time 30 =", x30)
print ("Y at time 30 =", y30)
print ("Z at time 30 =", z30)
print ("------------------")

t31 = 31 #time 31
h31 = (t31 - t13) / (t84 - t13) #contsant 31

x31 = x13 + h31 * (x84-x13) # x at time 31
y31 = y13 + h31 * (y84-y13) # y at time 31
z31 = z13 + h31 * (z84-z13) # z at time 31

print ("X at time 31 =", x31)
print ("Y at time 31 =", y31)
print ("Z at time 31 =", z31)
print ("------------------")

t32 = 32 #time 32
h32 = (t32 - t13) / (t84 - t13) #contsant 32

x32 = x13 + h32 * (x84-x13) # x at time 32
y32 = y13 + h32 * (y84-y13) # y at time 32
z32 = z13 + h32 * (z84-z13) # z at time 32

print ("X at time 32 =", x32)
print ("Y at time 32 =", y32)
print ("Z at time 32 =", z32)
print ("------------------")

t33 = 33 #time 33
h33 = (t33 - t13) / (t84 - t13) #contsant 33

x33 = x13 + h33 * (x84-x13) # x at time 33
y33 = y13 + h33 * (y84-y13) # y at time 33
z33 = z13 + h33 * (z84-z13) # z at time 33

print ("X at time 33 =", x33)
print ("Y at time 33 =", y33)
print ("Z at time 33 =", z33)
print ("------------------")

t34 = 34 #time 34
h34 = (t34 - t13) / (t84 - t13) #contsant 34

x34 = x13 + h34 * (x84-x13) # x at time 34
y34 = y13 + h34 * (y84-y13) # y at time 34
z34 = z13 + h34 * (z84-z13) # z at time 34

print ("X at time 34 =", x34)
print ("Y at time 34 =", y34)
print ("Z at time 34 =", z34)
print ("------------------")

t35 = 35 #time 35
h35 = (t35 - t13) / (t84 - t13) #contsant 35

x35 = x13 + h35 * (x84-x13) # x at time 35
y35 = y13 + h35 * (y84-y13) # y at time 35
z35 = z13 + h35 * (z84-z13) # z at time 35

print ("X at time 35 =", x35)
print ("Y at time 35 =", y35)
print ("Z at time 35 =", z35)
print ("------------------")

t36 = 36 #time 36
h36 = (t36 - t13) / (t84 - t13) #contsant 36

x36 = x13 + h36 * (x84-x13) # x at time 36
y36 = y13 + h36 * (y84-y13) # y at time 36
z36 = z13 + h36 * (z84-z13) # z at time 36

print ("X at time 36 =", x36)
print ("Y at time 36 =", y36)
print ("Z at time 36 =", z36)
print ("------------------")

t37 = 37 #time 37
h37 = (t37 - t13) / (t84 - t13) #contsant 37

x37 = x13 + h37 * (x84-x13) # x at time 37
y37 = y13 + h37 * (y84-y13) # y at time 37
z37 = z13 + h37 * (z84-z13) # z at time 37

print ("X at time 37 =", x37)
print ("Y at time 37 =", y37)
print ("Z at time 37 =", z37)
print ("------------------")

t38 = 38 #time 38
h38 = (t38 - t13) / (t84 - t13) #contsant 38

x38 = x13 + h38 * (x84-x13) # x at time 38
y38 = y13 + h38 * (y84-y13) # y at time 38
z38 = z13 + h38 * (z84-z13) # z at time 38

print ("X at time 38 =", x38)
print ("Y at time 38 =", y38)
print ("Z at time 38 =", z38)
print ("------------------")

t39 = 39 #time 39
h39 = (t39 - t13) / (t84 - t13) #contsant 39

x39 = x13 + h39 * (x84-x13) # x at time 39
y39 = y13 + h39 * (y84-y13) # y at time 39
z39 = z13 + h39 * (z84-z13) # z at time 39

print ("X at time 39 =", x39)
print ("Y at time 39 =", y39)
print ("Z at time 39 =", z39)
print ("------------------")

t40 = 40 #time 40
h40 = (t40 - t13) / (t84 - t13) #contsant 40

x40 = x13 + h40 * (x84-x13) # x at time 40
y40 = y13 + h40 * (y84-y13) # y at time 40
z40 = z13 + h40 * (z84-z13) # z at time 40

print ("X at time 40 =", x40)
print ("Y at time 40 =", y40)
print ("Z at time 40 =", z40)
print ("------------------")

t41 = 41 #time 41
h41 = (t41 - t13) / (t84 - t13) #contsant 41

x41 = x13 + h41 * (x84-x13) # x at time 41
y41 = y13 + h41 * (y84-y13) # y at time 41
z41 = z13 + h41 * (z84-z13) # z at time 41

print ("X at time 41 =", x41)
print ("Y at time 41 =", y41)
print ("Z at time 41 =", z41)
print ("------------------")

t42 = 42 #time 42
h42 = (t42 - t13) / (t84 - t13) #contsant 42

x42 = x13 + h42 * (x84-x13) # x at time 42
y42 = y13 + h42 * (y84-y13) # y at time 42
z42 = z13 + h42 * (z84-z13) # z at time 42

print ("X at time 42 =", x42)
print ("Y at time 42 =", y42)
print ("Z at time 42 =", z42)
print ("------------------")

t43 = 43 #time 43
h43 = (t43 - t13) / (t84 - t13) #contsant 43

x43 = x13 + h43 * (x84-x13) # x at time 43
y43 = y13 + h43 * (y84-y13) # y at time 43
z43 = z13 + h43 * (z84-z13) # z at time 43

print ("X at time 43 =", x43)
print ("Y at time 43 =", y43)
print ("Z at time 43 =", z43)
print ("------------------")

t44 = 44 #time 44
h44 = (t44 - t13) / (t84 - t13) #contsant 44

x44 = x13 + h44 * (x84-x13) # x at time 44
y44 = y13 + h44 * (y84-y13) # y at time 44
z44 = z13 + h44 * (z84-z13) # z at time 44

print ("X at time 44 =", x44)
print ("Y at time 44 =", y44)
print ("Z at time 44 =", z44)
print ("------------------")

t45 = 45 #time 45
h45 = (t45 - t13) / (t84 - t13) #contsant 45

x45 = x13 + h45 * (x84-x13) # x at time 45
y45 = y13 + h45 * (y84-y13) # y at time 45
z45 = z13 + h45 * (z84-z13) # z at time 45

print ("X at time 45 =", x45)
print ("Y at time 45 =", y45)
print ("Z at time 45 =", z45)
print ("------------------")

t46 = 46 #time 46
h46 = (t46 - t13) / (t84 - t13) #contsant 46

x46 = x13 + h46 * (x84-x13) # x at time 46
y46 = y13 + h46 * (y84-y13) # y at time 46
z46 = z13 + h46 * (z84-z13) # z at time 46

print ("X at time 46 =", x46)
print ("Y at time 46 =", y46)
print ("Z at time 46 =", z46)
print ("------------------")

t47 = 47 #time 47
h47 = (t47 - t13) / (t84 - t13) #contsant 47

x47 = x13 + h47 * (x84-x13) # x at time 47
y47 = y13 + h47 * (y84-y13) # y at time 47
z47 = z13 + h47 * (z84-z13) # z at time 47

print ("X at time 47 =", x47)
print ("Y at time 47 =", y47)
print ("Z at time 47 =", z47)
print ("------------------")

t48 = 48 #time 48
h48 = (t48 - t13) / (t84 - t13) #contsant 48

x48 = x13 + h48 * (x84-x13) # x at time 48
y48 = y13 + h48 * (y84-y13) # y at time 48
z48 = z13 + h48 * (z84-z13) # z at time 48

print ("X at time 48 =", x48)
print ("Y at time 48 =", y48)
print ("Z at time 48 =", z48)
print ("------------------")

t49 = 49 #time 49
h49 = (t49 - t13) / (t84 - t13) #contsant 49

x49 = x13 + h49 * (x84-x13) # x at time 49
y49 = y13 + h49 * (y84-y13) # y at time 49
z49 = z13 + h49 * (z84-z13) # z at time 49

print ("X at time 49 =", x49)
print ("Y at time 49 =", y49)
print ("Z at time 49 =", z49)
print ("------------------")

t50 = 50 #time 50
h50 = (t50 - t13) / (t84 - t13) #contsant 50

x50 = x13 + h50 * (x84-x13) # x at time 50
y50 = y13 + h50 * (y84-y13) # y at time 50
z50 = z13 + h50 * (z84-z13) # z at time 50

print ("X at time 50 =", x50)
print ("Y at time 50 =", y50)
print ("Z at time 50 =", z50)
print ("------------------")
