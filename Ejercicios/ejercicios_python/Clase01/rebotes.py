# rebotes.py
# Archivo de ejemplo
# Ejercicio
#Una pelota de goma es arrojada desde una altura de 100 metros y 
#cada vez que toca el piso salta 3/5 de la altura desde la que cayó.
# Escribí un programa rebotes.py que imprima una tabla mostrando
# las alturas que alcanza en cada uno de sus primeros diez rebotes.


altura_max = 100

rebote = 0

while rebote < 10:
    
     print(rebote, round(altura_max, 4)) 
     rebote+=1
     altura_max=altura_max*0.6
     