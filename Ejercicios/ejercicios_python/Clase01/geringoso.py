# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:51:27 2021

@author: santiago.espindola
"""

cadena = 'naranja'

capadepenapa = ''

for c in cadena:
   if c in 'aeiou':
       capadepenapa = capadepenapa + c + 'p' + c
   else: 
       capadepenapa = capadepenapa + c
       
print(capadepenapa)
    
        