
import csv
import pandas as pd
archivo = open('trabajando_txt\\archivo.txt',encoding='utf-8')
print(archivo.read()) #para abir el archivo

linea1 = archivo.readlines() # devuelve lo del archivo en listas 
linea = archivo.readline(10)
print(linea1)
print(linea)

with open('trabajando_txt\\archivo.csv', encoding='utf-8') as archive:
    reader = csv.reader(archive)
    for row in reader:
        print(row)

archivo = pd.read_csv('trabajando_txt\\archivo.csv')
print(archivo)

df = pd.read_csv('trabajando_txt\\archivo.csv')
nombre = df["nombre"]
print(nombre)