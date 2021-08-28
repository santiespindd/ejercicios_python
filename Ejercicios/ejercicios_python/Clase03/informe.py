# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:43:32 2021

@author: santiago.espindola
"""

import csv 



def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for i, fila in enumerate(rows, start=1):
            record = dict(zip(header, fila))
            try:
                record['nombre'] = record['nombre']
                record['cajones'] = int(record['cajones'])
                record['precio'] = float(record['precio'])
            except ValueError:
                print(f'Fila {i}: No pude interpretar: {fila}')
            camion.append(record)
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
    recaudacion = 0.0
    cantidad_cajones = {}
    
    for camion in camiones:
        costo_camion += int(camion[1]) * float(camion[2])
        if camion[0] in cantidad_cajones:
            cantidad_cajones[camion[0]] += camion[1]
        else:
            cantidad_cajones[camion[0]] = camion[1]
            
     
    for fov in camion:
        if fov in precios:
            recaudacion +=  precios[fov] * cantidad_cajones[fov]
       
    #pprint(cantidad_cajones)
    #pprint(precios)
        
    diferencia = recaudacion - costo_camion
   
    print(f'---Balance--- \n Costo del camion: ${costo_camion} \n Recaudación: ${recaudacion} \n Diferencia: ${diferencia:0.2f}')
    
balance()



