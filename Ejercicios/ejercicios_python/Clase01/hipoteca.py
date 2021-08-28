# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

pago_extra=1000 #Ejercicio 1.8

mes = 0

#Ejercicio 1.9

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108



while saldo > 0:
     saldo = saldo * (1+tasa/12) - pago_mensual
     total_pagado = total_pagado + pago_mensual 
       
     if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo -=  pago_extra
        total_pagado += pago_extra
       
     if saldo < 0:
       a_favor = saldo 
       saldo = 0
       total_pagado += a_favor   
    
     print(f'{mes+1} ${total_pagado:0.2f} ${saldo:0.2f}')
   
       
     mes+=1

print(f'Total pagado ${total_pagado:0.2f} Meses:{mes}')

#Total pagado 878712.08 Meses: 310