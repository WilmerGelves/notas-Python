import os 
cesto = []
opcion = 0
menu = '1. agregar producto\n2. eliminar producto\n3. modificar producto\n4. buscar producto\n5. total\n6. salir'
title = """
---------------------------
*    merca campusland     *
---------------------------
"""
while(opcion <6):
    print(title)
    print(menu)
    opcion = int(input(':)_'))
    match (opcion):
        case 1:
            isaddelement = True
            while (isaddelement):
                os.system('cls')
                nombre = input('ingrese el nombre del producto :').upper()
                valor = float(input(f'ingrese el valor de {nombre}: '))
                cantidad = int(input(f'ingresa cantida de {nombre}: '))
                producto = [nombre,valor,cantidad]
                cesto.append(producto)
                isaddelement = bool(input('desea agregar otro poducto....s(si)o enter(no)'))
        case 2:
            palabra = input ('ingrese el nombre del producto a borrar: ').upper()
            for i,item in enumerate(cesto):
                if palabra in item:
                    cesto.pop(i)
                    break
            print(cesto)
            os.system('pause')
        case 3:
            palabra = input ('ingrese el nombre del producto a modificar').upper()
            for i,item in enumerate(cesto):
                if palabra in item:
                    if(bool(input('desea modificar el nombre del producto....s(si)o enter(no)'))):
                        item[0] = input('ingrese el nuevo nombre').upper()
                    if(bool(input('desea modificar el precio del producto....s(si)o enter(no)'))):
                        item[1] = float(input('ingrese el nuevo precio de {item[0]} :'))
                    if(bool(input('desea modificar la cantida del producto....s(si)o enter(no)'))):
                        item[2] = int(input('ingrese la nuevo cantidad {item[0]}:'))
        case 4:
            os.system('cls')
            palabra = input('ingre el nombre del producto a buscar:').upper
            for i,item in enumerate(cesto):
                if palabra in item:
                    print (f'nombre del producto:{item[0]}')
                    print (f'precio del producto: {item[1]}')
                    print (f'cantidad disponible del prodcuto : {item[2]}')
            print(cesto)
            os.system('pause')
        case 5:
            os.system('cls')
            print("Resumen de Productos:")
            total_valor = 0
            for item in cesto:
                nombre, precio, cantidad = item
                total_producto = precio * cantidad
                total_valor += total_producto
                print(f"Nombre: {nombre}, Precio: {valor}, Cantidad: {cantidad}, Total: {total_producto}")
            print(f"Valor Total de Productos: {total_valor}")
            os.system('pause')
        case 6:
            os.system('cls') 

        case _:
            print("Seleccion no válida")
            os.system('pause')
            opcion = 0