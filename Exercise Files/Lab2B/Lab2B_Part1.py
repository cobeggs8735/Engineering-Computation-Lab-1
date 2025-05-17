# -*- coding: utf-8 -*-
"""
Coleman Beggs

UIN: 326009580

ENGR: 102 - 509

I'm a world champion robot driver.

"""
#Equation Calculator

import math

print ()
print ("Coleman Beggs")
print ("ENGR: 102-509")
print ("I'm a world champion robot driver.")

# Ohm's Law
print ()
print ("Ohm's Law")

R = 20 #resistance
I = 5 #Current
V = R * I #Voltage

print ("Resistance =", R, "Ohms")
print ("Current =", I, "Amps")
print ("Voltage =", V, "Volts")

# KineticEnergy
print ( )
print ("Kinetic Energy")

m_kilos = 100 #Mass in Kilogams
v = 21 #Velocity
ke = m_kilos/2 * v ** 2 #Kinetic Energy

print ("Mass =", m_kilos, "kg") 
print ("Velocity =", v, "m/s") #meters per second
print ("Kinetic Energy", ke, "Joules") #Joules

# Reynolds Number 
print ()
print ("Reynolds Number")

v = 100 #m/s
L = 2.5 #m
kv = 1.2 #m^2/s
Re = (v * L) / kv

print ("Velocity =", v, "m/s")
print ("Characteristic Linear Dimension", L, "Meters")
print ("Kinematic Viscosity", kv, "m^2/s")
print ("Reynolds Number", Re)

# Stefan-Boltzmann Law
print ()
print ("Stefan-Boltzmann Law")

Constant = 5.67E-8 #watt / m^sK^4
T = 2200 #Kelvin
F = Constant * math.pow(T, 4) #Energy Flux

print ("Stefan-Boltzmann Constant =", Constant, "watt / m^sK^4") #Watt per m^sK^4
print ("Temperature =", T, "Kelvin") #Kelvin
print ("Energy Flux", F) 

# Arps Equation
print ()
print ("Arps Equation")

b = 0.8 #Hyperbolic Constant
D = 2 #Initial Decline Rate per Day
t = 20 #Days
q = 100 #Initial Production Rate
Q = q/(1 + D * t) ** (1/b) #Current Production Rate

print ("Hyperbolic Constant =",b) #Constant
print ("Initial Decline Rate =", D, "per day") #Per Day
print ("Time =", t, "Days") #Days
print ("Initial Production Rate", q) #Rate
print ("Current Production Rate =", Q, "per day") #Per Day

# M/M/1 Queue
print ()
print ("M/M/1/Queue")

λ = 20 #Arrival Rate
μ = 35 #Service Rate
ρ = λ / μ #Utilization of System
Lq = ρ**2 / (1 - ρ) #Mean Number of Customers in the Queue
Wq = Lq / λ #Mean Wait in the Queue
W = Wq + (1/μ) #Mean Wait in the System

print (λ, "Arrival Rate")
print (µ, "Service Rate")
print (Lq, "Mean Number of Customers in the Queue")
print (Wq, "Wait in the Queue")
print (W, "Mean Wait in the System")

# Mohr-Coulomb Failure Criterion
print ()
print ("Mohr-Coulomb Failure Criterion")

σ = 20 #Normanl Stress
c = 2 #Cohesion
θ = 35 #Angle of Internal Friction
Γ = c + (σ * math.degrees(math.tan(θ))) #Shear Strength

print (σ,"Normal Stress") #No Units
print (c, "Cohesion") #No Units
print ("Angle of Interal Friction =", θ, "Degrees")
print (Γ, "Shear Strength") #No Units

# Bragg’s Law
print ()
print ("Bragg’s Law")

λ = 7.5E-07 #Wavelength of Light in nm
d = 1E-06 #Lattice in nm
n = 1 #Order
θ = math.degrees(math.asin((n * λ) / (2 * d))) #Angle of Interference in Degrees

print ("Wavelength =", λ, "nm") #Nanometers
print ("Lattice =", d, "nm") #Nanometers
print ("Order =", n) #No Units
print ("Angle of Interference", θ, "Degrees") #Degrees
