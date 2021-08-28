'''

f = open('../Data/precios.csv', 'rt')


naranja = ''

next(f).split(',')

for line in f:
        
        row = line.split(',')
        if row[0] == 'Naranja':
            naranja = row[1]
       
f.close()

print(naranja)
'''

numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')