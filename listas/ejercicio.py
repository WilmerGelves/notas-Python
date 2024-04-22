import os
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input(f'Nombre del {i+1} compañero:  ')
        edad = int(input('Edad: '))
        os.system('cls')
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1]) #donde key es el parametro por el que se va ordenar la tupla. y  la tupla compañero es(0,1) por eso se pasa uno.
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente,profesor = obtener_compañeros(5)
print(f'El profesor es {profesor} y el asistente es {asistente}')