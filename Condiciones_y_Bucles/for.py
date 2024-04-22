nombres = ['William','Galindo','isabel']

for nombre in enumerate(nombres):
    indice = nombre[0]
    valor = nombre[1]
    print(f'En el indice {indice+1} esta {valor}')


numeros = [1,2,3,4,5,6,7,8,9]
numeros2 = [1,2,3,4,5,6,7,8,9]

for numeros,numeros2  in zip(numeros,numeros2): #para iterar mas de una lista a la vez
    print(f'{numeros},{numeros2}')


nombres = ['luis','carlos','omar']

for nombre in enumerate(nombres):
    indice = nombre[0]
    valor = nombre[1]
    print (f'El nombre {valor} esta en el indice {indice + 1}	')