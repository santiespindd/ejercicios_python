#Informe.py
from pprint import pprint #  Se usó solo para debuguear, pero por las dudas la dejo
import csv

def leer_camion(nombre_archivo):
	camion = {}
	lista = []
	with open(nombre_archivo, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			#camion["nombre"] = row[0]
			#camion["cajones"] = int(row[1])
			#camion["precio"] = float(row[2])
			lote = (row[0], row[1], row[2])
			headers = ("Nombre","Cajones","Precio")
			camion = {
				headers[0] : lote[0],
				headers[1] : lote[1],
				headers[2] : lote[2],
			}
			lista.append(camion)
			
	return lista

def leer_precios(nombre_archivo):
	dicc = {} #  Dicc corresponde a Diccionario
	f = open(nombre_archivo, "rt")
	for line in f:
		row = line. split(",")
		try:
			dicc[row[0]] = row[1].strip()
		except IndexError:
			break
	f.close()
	return(dicc)


precios = leer_precios("../Data/precios.csv")

camion = leer_camion("../Data/camion.csv")

costoCamion = 0.0
recaudadoVenta = 0.0
gananciaTotal = 0.0

for art in camion:
	nombreC = art["Nombre"] #C corresponde a Camión
	precioC = float(art["Precio"]) #  C corresponde a Camión
	cajonesC = int(art["Cajones"]) #  C corresponde a Camión
	costoCamion += precioC * cajonesC
	recaudadoVenta += float(precios[nombreC]) * cajonesC
	gananciaArt = float(precios[nombreC]) - precioC #  Art corresponde a Artículo
	gananciaArts = gananciaArt * cajonesC #  Arts corresponde a Artículos
	gananciaTotal += gananciaArts
	
print("Costo total del camión:",round(costoCamion,2))
print("Total recaudado:",round(recaudadoVenta,2))
print("Ganancia total del negocio:", round(gananciaTotal,2))
