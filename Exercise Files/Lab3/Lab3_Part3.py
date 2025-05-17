#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:42:52 2019

@author: colemanbeggs
"""

HumanName = str(input("Give me a name \n"))
TimeTravel = float(input("Give me a time in hours\t"))
TimeTraveled = TimeTravel*60
OutdoorLocation = str(input("Give me a Outdoor location or location\'s"))
Creature= str(input("Give me a animal or some sort of \" creature\""))
Mood = str(input("give me a mood\n"))
adjective = str(input("give me an adjective\t"))
print(HumanName,TimeTraveled,OutdoorLocation,Creature,Mood,adjective)
print(HumanName,"tried going to the post office in",OutdoorLocation,"It only took them",TimeTraveled,"minutes to get there but he had trouble"
" getting inside the store when a " ,Creature,"tried tying them to a cars hood and running him into a horse's yacht in the swimming pool.\n"
"This made",HumanName,Mood,"because the ",Creature,"wasnt even all that",adjective,"looking to make up for it so\n",HumanName,"went home and never went outside is rock made house again")
