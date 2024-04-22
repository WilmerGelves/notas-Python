
diccionario = {
    'nombre': 'lucas',
    'apellidos': 'gelves',
    'subs': 0,
}

#Funciones diccionarios.
claves = diccionario.keys() #devuelve las claves, tambien sirve para iterar.
valor = diccionario.get('nombre') #Devuelve el valor de una llave 
valores = diccionario.items()  #deuvlve la clave y el valor 

print(valores)

#form a de iterar un diccionario para obtener claves 
for key in diccionario:
    print(key)


#forma de iterar para obtener claves y valores
for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f'{key}; {valor}' )