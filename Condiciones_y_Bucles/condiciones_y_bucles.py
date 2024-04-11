#Condicionales

# -*- coding: utf-8
semaforo = 'verde'

if semaforo == 'verde': 
    print("Cruzar la calle")

else: print("Esperar")

#Ejemplo:
compra = 250 
if compra <= 100: 
    print ("Pago en efectivo")

elif compra >100 and compra<=300:
    print("Pago con tarjeta débito")

else: print("Pago con tarjeta de crédito")

#BUCLE WHILE
anio = 2001
while anio <= 2012:
    print("informes del año", str(anio))
    anio = anio + 1


#BUCLE FOR 
mi_lista = ['juan', 'pedro', 'alicia','edi']
for nombre in mi_lista:
    print(nombre)