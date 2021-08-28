# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:57:48 2021

@author: santiago.espindola
"""

#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()

#Errores: 
    #No recorre toda la expresión
    #No considera 'a' mayúsculas
    
#Solución --> Quito el return False y lo agrego fuera del while 
#             Agrego lower()

def tiene_a(expresion):
       n = len(expresion)
       i = 0
       while i<n:
           if expresion[i].lower() == 'a':
              return True
           i += 1
       return False
tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente

#Errores:
# mal definicion funcion         
# error en while           
# error en if            
# asignacion en vez de equidad    
# error tipeo  
# no considera 'a' mayusculas

#Solucion
#agrego ":"
#agrego ":"
#agrego  ":"
#cambio el "=" por "=="
#cambio Falso por False
#agrego lower()



def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))


                     
#%%
#Ejercicio 3.3. Función tiene_uno()

#Error:
#No se puede aplicar un len a un int 
#Solucion
#parsear el int a str


def tiene_uno(expresion):
    if type(expresion) == int:
        expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
#Ejercicio 3.4: Alcances
#Error:
#falta return en la función

#Solucion
def suma(a,b):
     c = a + b
     return c
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%

#Ejercicio 3.5: Pisando memoria¶

#Error : se pisa registro{} en el for
#Solucion : agregar registro dentro del for

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
   
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

