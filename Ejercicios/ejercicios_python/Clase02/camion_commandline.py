# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:14:37 2021

@author: santiago.espindola
"""

import csv
import sys

def costo_camion(nombre_archivo):
    f = open('../Data/camion.csv', 'rt')
    
    rows = csv.reader(f)
    costo_camion = 0
    
    next(f).split(',')
    
    for row in rows:
            
            costo_camion = costo_camion + int(row[1]) * float(row[2])
           
    f.close()
    
    return costo_camion


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)

print('Costo total:', costo)
