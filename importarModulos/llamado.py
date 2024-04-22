#Si quiero hacer llamado de la funcion
from funciones import saludo
saludo = saludo('Wilmer','Gelves')
print(saludo)

#Si quiero importar la funcion
import funciones as hola
saludo = hola.saludar_raro('Wilmer')
print(saludo)