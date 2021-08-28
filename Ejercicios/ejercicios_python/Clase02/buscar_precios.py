# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:34:40 2021

@author: santiago.espindola
"""

def buscar_precio(fruta): 

    f = open('../Data/precios.csv', 'rt')

    costo = 0
    for line in f:
        row = line.split(',')
        if row[0].lower() == fruta.lower(): 
                costo = float(row[1])
                print(f'El precio de un cajón de {fruta} es : ${costo}')
    if costo == 0:
        print(f'{fruta} no figura en el listado de precios.')
            
    f.close()
    


buscar_precio('naranja')