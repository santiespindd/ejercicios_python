# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:46:15 2021

@author: santiago.espindola
"""
import csv

f = open('../Data/camion.csv', 'rt')

rows = csv.reader(f)
costo_camion = 0

next(f).split(',')

for row in rows:
        
        costo_camion = costo_camion + int(row[1]) * float(row[2])
       
f.close()

print(f'Costo Total: {costo_camion}')