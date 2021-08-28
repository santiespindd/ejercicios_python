# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:09:50 2021

@author: santiago.espindola
"""


import math

radio = input("Ingrese el radio de la esfera: ")


volumen = (4/3)*(math.pi)*(float(radio)**3)            #4/3 πr^3. 

print("El volumen es: " , round(volumen,2))