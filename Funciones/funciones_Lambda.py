
#son funciones anónimas 
numeros = [1,2,3,4,5,6,7,8,9,10]

#numeros pares con una funcion lambda
pares = filter(lambda numero: numero%2 == 0, numeros)
print(list(pares))