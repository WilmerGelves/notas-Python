""" Una función, es la forma de agrupar expresiones y sentencias (algoritmos) que realicen determinadas acciones, pero que éstas solo se ejecuten cuando son llamadas."""

#Ejemplo: la funcion puede retornar un valor y éste se puede almacenar en una variable para visualizarlo.

def saludo1():
    print("Hola mundo")

saludo1()

#ó
def saludo():
    return "Bienvenido al sistema"


saludo = saludo()
print(saludo)



#DEFINICION DE FUNCIONES CON PARÁMETROS
def mi_funcion(nombre,apellido):
    nombre_completo = nombre, apellido
    print(nombre_completo)

mi_funcion('Wilmer','Gelves')




