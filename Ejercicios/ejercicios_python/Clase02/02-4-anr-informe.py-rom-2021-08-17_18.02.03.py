# fragmento de costo_camion.py
from pprint import pprint
import csv

#Arma los precios como datos dentro de un diccionario:
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except:
                pass    
    return precios

#Arma los lotes como diccionarios dentro de una lista:
def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = {"nombre": row[0],
                    "cajones": int(row[1]),
                    "precio": float(row[2])}
            camion.append(lote)
    return camion

# Conformo las ventas del camión como lista
camion = leer_camion("../Data/camion.csv")

# Armo un diccionario con la lista de precios
precios = leer_precios("../Data/precios.csv")

totalventa = 0.0
totalcosto = 0.0

#Recorro todos los elementos del camión, determino su costo y busco 
#el nombre en la lista de precios
for s in camion:
    totalcosto += s['cajones'] * s['precio']
    totalventa += s['cajones'] * precios[s["nombre"]]

#Muestro en pantalla el balance, con tabulaciones para su mejor lectura.

print(f'Costo:\t\t\t{round(totalcosto,2)}' )
print(f'Ventas:\t\t\t{round(totalventa,2)}')
print('\t' *3 + '-' * 10)

if totalventa - totalcosto > 0:
    print(f'Hubo ganancias por:\t {round(totalventa - totalcosto,2)}')
elif totalventa - totalcosto < 0:
    print(f'Hubo pérdidas por:\t {round(totalventa - totalcosto,2)}')
else:
    print(f'No hubo pérdidas ni ganancias, el balance cerró en 0 (cero)')