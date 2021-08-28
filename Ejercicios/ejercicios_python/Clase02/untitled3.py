# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:49:37 2021

@author: santiago.espindola
"""

def buscar_precio(fov):
    precio_u = False
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:
            row = line.strip('\n').split(',')
            if row[0].lower() == fov.lower():
                precio_u = float(row[1])
                print(f'[{fov:^12s}]: {precio_u}')  
        if precio_u is False:
            print(f'{fov} no figura en el listado de precios')
    

buscar_precio('asdads')