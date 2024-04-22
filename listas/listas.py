#identificador
frutas = [] #lista vacía 
verduras = ['tomate', 'cebolla','puerro']
print(len(verduras))
print(verduras[1]) #Indexar un elemento de la lista.

#CICLOS EN ESTRUCTURA DE DATOS
for verdura in verduras: #recorrer una lista.
    print(verdura)

#Agregar elementos a la lista 
frutas.append('fresa')
print(frutas)
frutas.append(input('Nombre de la fruta:'))
print(frutas)

#Eliminar elementos a la lista
frutas.remove('fresa')#elimina basado en un elemento en específico
print(frutas)
dato = frutas.pop(0) #Elimina basado en su indice  y permite recuperar la info almacenandola en una variable,por ejemplo:
frutas.append(dato)   
print(frutas)


#Para recorrer dos o mas listas a la vez
animal = ['gato','perro','iguana']
numeros = [1,2,3,]
for animal,numeros in zip(animal,numeros):
    print(animal)
    print(numeros)


#Funciones con listas adicionales
lista = list([1,3,2,4,5]) #crea una lista 

lista.insert(0,'inicio de la lista') #Agrega elementos en el indice indicado

lista.extend([6,7]) #Agrega mas de un elemento al final de la lista

print(lista)

lista.remove('inicio de la lista') #Elimina elemnetos por su contenido.

lista.sort() #Ordena los elementos. si usamos dentro de la funcion true=reverse, invierte el orden. 
print(lista)
lista.sort(reverse=True) 
print(lista)
valor = lista.index(1) #Busca un valor en específico dentro de la lista y me devuelve su indice o posicion 
print(valor)