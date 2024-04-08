"""DATOS COMPLEJOS

->TUPLAS: Una tupla es una variable que permite almacenar varios datos inmutables (no pueden
ser modificados una vez creados) de tipos diferentes:
"""
mi_tupla = ('cadena de texto', 15, 2.8,'otro dato',25)
#Para acceder a un dato de la tupla se hace mediante su índice, teneiendo en cuenta que su índice inicial es cer.Ejemplo 

print(mi_tupla[0])
# o para acceder a una porcioón de la tupla lo hacemos de la siguiente forma
print(mi_tupla[0:2])

"""LISTAS: Una lista es similar a una tupla con la diferencia fundamental de que permite modificar los
datos una vez creados.Se accede igual que las tuplas. EJEMPLO"""

mi_lista = [1,2,3,4,5]
print(mi_lista[1])
mi_lista[1] = 3
print(mi_lista[1])

"""DICCIONARIOS: Mientras que a las listas y tuplas se accede solo y únicamente por un número de índice,
los diccionarios permiten utilizar una clave para declarar y acceder a un valor:"""

mi_diccionario = {'user1': "Wilmer", 'user2' : "Carlos", 'user3': "Edy", 'user4': "Rosa"}
print(mi_diccionario['user1'])
mi_diccionario['user1'] = "Omar"
print(mi_diccionario['user1'])
