# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:29:13 2021

@author: santiago.espindola
"""

def traductor_geringoso(cadena):
    
    capadepenapa = ''

    for c in cadena:
        if c in 'aeiouAEIOU':
           capadepenapa = capadepenapa + c + 'p' + c
        else: 
           capadepenapa = capadepenapa + c
           
    return capadepenapa         

def diccionario_geringoso(lista):
    
    diccionario = {}
     
    for cadena in lista:
        diccionario[cadena] =  traductor_geringoso(cadena)
    
    print(diccionario)
    
    
lista = ['banana', 'manzana', 'mandarina']
    
diccionario_geringoso(lista)