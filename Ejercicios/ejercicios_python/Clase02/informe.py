# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:53:39 2021

@author: santiago.espindola
"""
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
     camion=[]

     with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
             lote = (row[0], int(row[1]), float(row[2]))
             camion.append(lote)
     return camion
 
    
def leer_precios(nombre_archivo):
     precios={}

     with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
             try:
                 precios[row[0]] = float(row[1])
             except:
                 pass
        return precios
    

def balance():
    camiones= leer_camion('../Data/camion.csv')
    precios= leer_precios('../Data/precios.csv')
    
    costo_camion = 0.0
    total_venta = 0.0
    cant_cajones = {}
    
    for fov in camiones:
        costo_camion += int(fov[1]) * float(fov[2])
        if fov[0] in precios.keys():
            total_venta += precios[fov[0]] * fov[1]
        
                                                         
    print(costo_camion)
    print(total_venta)
    pprint(camiones)
    
    
balance()

    
    
    

    
    
    