#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:16:06 2019

@author: colemanbeggs
"""

#Formula for pounds
"""
Formula: weight (lb) / [height (in)]2 x 703
Calculate BMI by dividing weight in pounds (lbs) by height in inches (in) squared
and multiplying by a conversion factor of 703.

Example: Weight = 150 lbs, Height = 5’5″ (65″)
Calculation: [150 ÷ (65)2] x 703 = 24.96
"""
#Formula for kilograms
"""
Formula: weight (kg) / [height (m)]2
With the metric system, the formula for BMI is weight in kilograms divided by 
height in meters squared. Because height is commonly measured in centimeters, 
divide height in centimeters by 100 to obtain height in meters.

Example: Weight = 68 kg, Height = 165 cm (1.65 m)
Calculation: 68 ÷ (1.65)2 = 24.98
"""



#Input height
height = float(input("Input your height: ", ))
heightUnit = input("Input a unit for height (meters or inches): ", )

#Input weight
weight = float(input("Input your weight: ", ))
weightUnit = input("Input a uit for weight (pounds or kilograms): ", )

if((heightUnit=="Meters")or(heightUnit=="meters")or(heightUnit=="m"))and((weightUnit=="Kilograms")or(weightUnit=="kilograms")or(weightUnit=="kg")):
    bmi = weight / height**2
elif((heightUnit=="Inches")or(heightUnit=="inches")or(heightUnit=="in"))and((weightUnit=="Pounds")or(weightUnit=="pounds")or(weightUnit=="lbs")):
    bmi = (weight / height**2) * 703
else:
    print ("Invalid unit input")
    
print ("Weight =", weight, weightUnit)
print ("Height =", height, heightUnit)
print ("BMI =", bmi)

#Weight Status
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi <= 24.9:
    status = "Healthy Weight"
elif 25.0 <= bmi <= 29.9:
    status = "Overweight"
elif bmi >= 30.0:
    status = "Obese"

print("Weight Status:", status)

































