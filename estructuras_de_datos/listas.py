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
