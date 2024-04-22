import os
def AddProduct(canasta : list):
        isaddelement = True
        while (isaddelement):
            os.system('cls')
            nombre = input('ingrese el nombre del producto :').upper()
            valor = float(input(f'ingrese el valor de {nombre}: '))
            cantidad = int(input(f'ingresa cantida de {nombre}: '))
            producto = [nombre,valor,cantidad]
            canasta.append(producto)
            isaddelement = bool(input('desea agregar otro poducto....s(si)o enter(no)'))

def SearchElemnt(canasta : list):
    palabra = input ('ingrese el nombre del producto a borrar: ').upper()
    for i,item in enumerate(canasta):
        if palabra in item:
            return [i,item]