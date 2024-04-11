#Ejercicio que permite calcular el monto a pagar por un usuario.
import os
if __name__ == "__main__":
    productos = 0.0
    efectivo = 0.0
    nombreUsuario = ''

    nombreUsuario = str(input('Ingrese el nombre del usuario: '))
    os.system('cls')
    for i in range(0,10,1):
        if(i<=10):
            productos += float(input(f'Ingrese el monto del producto Nro{i+1}: '))
    print(f'Monto a pagar: {productos}')
    efectivo = float(input('Monto recibido: '))
    print(f'Señor {nombreUsuario} su cambio es: {efectivo-productos} ')
