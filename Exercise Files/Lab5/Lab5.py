#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:52:28 2019

@author: colemanbeggs
"""

sex = input("Enter your gender ('m' for male, 'f' for female): ",)
age = int(input("Enter your age(20 to 79): ",))
t_chol = float(input("Enter your total cholesterol: ",))
smoker = bool(input("Enter if you smoke True or False: ",))
HDL_chol = float(input("Enter your HDL cholesterol: ",))
TBP = bool(input("Enter if your systolic blood pressure is being treated: ",))
SBP = int(input("Enter your systolic blood pressure: ",))

#Male
if sex == 'm':
    if 20 <= age <= 34:
        points = -9
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 4
        elif 200 <= t_chol <= 239:
            t_points = points + 7
        elif 240 <= t_chol <= 279:
            t_points = points + 9
        elif t_chol >= 280:
            t_points = points + 11
            
        if smoker == True:
            t_points += 8
        else:
            t_points += 0
            
    elif 35 <= age <= 39:
        points = -4
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 4
        elif 200 <= t_chol <= 239:
            t_points = points + 7
        elif 240 <= t_chol <= 279:
            t_points = points + 9
        elif t_chol >= 280:
            t_points = points + 11
            
        if smoker == True:
            t_points += 8
        else:
            t_points += 0
            
    elif 40 <= age <= 44:
        points = 0
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 3
        elif 200 <= t_chol <= 239:
            t_points = points + 5
        elif 240 <= t_chol <= 279:
            t_points = points + 6
        elif t_chol >= 280:
            t_points = points + 8
            
        if smoker == True:
            t_points += 5
        else:
            t_points += 0
            
    elif 45 <= age <= 49:
        points = 3
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 3
        elif 200 <= t_chol <= 239:
            t_points = points + 5
        elif 240 <= t_chol <= 279:
            t_points = points + 6
        elif t_chol >= 280:
            t_points = points + 8
            
        if smoker == True:
            t_points += 5
        else:
            t_points += 0
            
    elif 50 <= age <= 54:
        points = 6
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 2
        elif 200 <= t_chol <= 239:
            t_points = points + 3
        elif 240 <= t_chol <= 279:
            t_points = points + 4
        elif t_chol >= 280:
            t_points = points + 5
            
        if smoker == True:
            t_points += 3
        else:
            t_points += 0
            
    elif 55 <= age <= 59:
        points = 8
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 2
        elif 200 <= t_chol <= 239:
            t_points = points + 3
        elif 240 <= t_chol <= 279:
            t_points = points + 4
        elif t_chol >= 280:
            t_points = points + 5
            
        if smoker == True:
            t_points += 3
        else:
            t_points += 0
            
    elif 60 <= age <= 64:
        points = 10
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 1
        elif 200 <= t_chol <= 239:
            t_points = points + 1
        elif 240 <= t_chol <= 279:
            t_points = points + 2
        elif t_chol >= 280:
            t_points = points + 3
            
        if smoker == True:
            t_points += 1
        else:
            t_points += 0
            
    elif 65 <= age <= 69:
        points = 11
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 1
        elif 200 <= t_chol <= 239:
            t_points = points + 1
        elif 240 <= t_chol <= 279:
            t_points = points + 2
        elif t_chol >= 280:
            t_points = points + 3
            
        if smoker == True:
            t_points += 1
        else:
            t_points += 0
            
    elif 70 <= age <= 74:
        points = 12
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 0
        elif 200 <= t_chol <= 239:
            t_points = points + 0
        elif 240 <= t_chol <= 279:
            t_points = points + 1
        elif t_chol >= 280:
            t_points = points + 1
            
        if smoker == True:
            t_points += 1
        else:
            t_points += 0
            
    elif 75 <= age <= 79:
        points = 13
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 0
        elif 200 <= t_chol <= 239:
            t_points = points + 0
        elif 240 <= t_chol <= 279:
            t_points = points + 1
        elif t_chol >= 280:
            t_points = points + 1
            
        if smoker == True:
            t_points += 1
        else:
            t_points += 0
            
    else:
        print ("Cannot compute risk")
        
    if HDL_chol >= 60:
        t_points += -1
    elif 50 <= HDL_chol <= 59:
        t_points += 0
    elif 40 <= HDL_chol <= 49:
        t_points += 0
    else:
        t_points += 2
        
    if TBP == True:
        if SBP < 120:
            t_points += 0
        elif 120 <= SBP <= 129:
            t_points += 1
        elif 130 <= SBP <= 139:
            t_points += 2
        elif 140 <= SBP <= 159:
            t_points += 2
        else:
            t_points += 3
    else:
        if SBP < 120:
            t_points += 0
        elif 120 <= SBP <= 129:
            t_points += 0
        elif 130 <= SBP <= 139:
            t_points += 1
        elif 140 <= SBP <= 159:
            t_points += 1
        else:
            t_points += 2
            
    if t_points < 0:
        risk = "<1%"
    elif 0 <= t_points <= 4:
        risk = "1%"
    elif 5 <= t_points <= 6:
        risk = "2%"
    elif t_points == 7:
        risk = "3%"
    elif t_points == 8:
        risk = "4%"
    elif t_points == 9:
        risk = "5%"
    elif t_points == 10:
        risk = "6%"
    elif t_points == 11:
        risk = "8%"
    elif t_points == 12:
        risk = "10%"
    elif t_points == 13:
        risk = "12%"
    elif t_points == 14:
        risk = "16%"
    elif t_points == 15:
        risk = "20%"
    elif t_points == 16:
        risk = "25%"
    elif t_points == 17:
        risk = "30%"
    else:
        risk = ">30%"

# Female            
elif sex == 'f':
    if 20 <= age <= 34:
        points = -7
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 4
        elif 200 <= t_chol <= 239:
            t_points = points + 8
        elif 240 <= t_chol <= 279:
            t_points = points + 11
        elif t_chol >= 280:
            t_points = points + 13
            
        if smoker == True:
            t_points += 9
        else:
            t_points += 0
            
    elif 35 <= age <= 39:
        points = -3
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 4
        elif 200 <= t_chol <= 239:
            t_points = points + 8
        elif 240 <= t_chol <= 279:
            t_points = points + 11
        elif t_chol >= 280:
            t_points = points + 13
            
        if smoker == True:
            t_points += 9
        else:
            t_points += 0
            
    elif 40 <= age <= 44:
        points = 0
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 3
        elif 200 <= t_chol <= 239:
            t_points = points + 6
        elif 240 <= t_chol <= 279:
            t_points = points + 8
        elif t_chol >= 280:
            t_points = points + 10
            
        if smoker == True:
            t_points += 7
        else:
            t_points += 0
            
    elif 45 <= age <= 49:
        points = 3
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 3
        elif 200 <= t_chol <= 239:
            t_points = points + 6
        elif 240 <= t_chol <= 279:
            t_points = points + 8
        elif t_chol >= 280:
            t_points = points + 10
            
        if smoker == True:
            t_points += 7
        else:
            t_points += 0
            
    elif 50 <= age <= 54:
        points = 6
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 2
        elif 200 <= t_chol <= 239:
            t_points = points + 4
        elif 240 <= t_chol <= 279:
            t_points = points + 5
        elif t_chol >= 280:
            t_points = points + 7
            
        if smoker == True:
            t_points += 4
        else:
            t_points += 0
            
    elif 55 <= age <= 59:
        points = 8
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 2
        elif 200 <= t_chol <= 239:
            t_points = points + 4
        elif 240 <= t_chol <= 279:
            t_points = points + 5
        elif t_chol >= 280:
            t_points = points + 7
            
        if smoker == True:
            t_points += 4
        else:
            t_points += 0
            
    elif 60 <= age <= 64:
        points = 10
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 1
        elif 200 <= t_chol <= 239:
            t_points = points + 2
        elif 240 <= t_chol <= 279:
            t_points = points + 3
        elif t_chol >= 280:
            t_points = points + 4
            
        if smoker == True:
            t_points += 2
        else:
            t_points += 0
            
    elif 65 <= age <= 69:
        points = 12
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 1
        elif 200 <= t_chol <= 239:
            t_points = points + 2
        elif 240 <= t_chol <= 279:
            t_points = points + 3
        elif t_chol >= 280:
            t_points = points + 4
            
        if smoker == True:
            t_points += 2
        else:
            t_points += 0
            
    elif 70 <= age <= 74:
        points = 14
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 1
        elif 200 <= t_chol <= 239:
            t_points = points + 1
        elif 240 <= t_chol <= 279:
            t_points = points + 2
        elif t_chol >= 280:
            t_points = points + 2
            
        if smoker == True:
            t_points += 1
        else:
            t_points += 0
            
    elif 75 <= age <= 79:
        points = 16
        if t_chol < 160:
            t_points = points + 0
        elif 160 <= t_chol <= 199:
            t_points = points + 1
        elif 200 <= t_chol <= 239:
            t_points = points + 1
        elif 240 <= t_chol <= 279:
            t_points = points + 2
        elif t_chol >= 280:
            t_points = points + 2
            
        if smoker == True:
            t_points += 1
        else:
            t_points += 0
            
    else:
        print ("Cannot compute risk")
        
    if HDL_chol >= 60:
        t_points += -1
    elif 50 <= HDL_chol <= 59:
        t_points += 0
    elif 40 <= HDL_chol <= 49:
        t_points += 1
    else:
        t_points += 2
        
    if TBP == True:
        if SBP < 120:
            t_points += 0
        elif 120 <= SBP <= 129:
            t_points += 3
        elif 130 <= SBP <= 139:
            t_points += 4
        elif 140 <= SBP <= 159:
            t_points += 5
        else:
            t_points += 6
    else:
        if SBP < 120:
            t_points += 0
        elif 120 <= SBP <= 129:
            t_points += 1
        elif 130 <= SBP <= 139:
            t_points += 2
        elif 140 <= SBP <= 159:
            t_points += 3
        else:
            t_points += 4
            
    if t_points < 9:
        risk = "<1%"
    elif 9 <= t_points <= 12:
        risk = "1%"
    elif 13 <= t_points <= 14:
        risk = "2%"
    elif t_points == 15:
        risk = "3%"
    elif t_points == 16:
        risk = "4%"
    elif t_points == 17:
        risk = "5%"
    elif t_points == 18:
        risk = "6%"
    elif t_points == 19:
        risk = "8%"
    elif t_points == 20:
        risk = "11%"
    elif t_points == 21:
        risk = "14%"
    elif t_points == 22:
        risk = "17%"
    elif t_points == 23:
        risk = "22%"
    elif t_points == 24:
        risk = "27%"
    elif t_points == 25:
        risk = "30%"
    else:
        risk = ">30%"

#Not Male or Female    
else:
    print ("Invalid gender input")
    
print ("Risk of heart disease is:", risk)