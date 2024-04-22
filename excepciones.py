def suma():
    while True:
        a = input('Numero a: ')
        b = input('Numero b: ')
        try: 
            sumar = int(a) + int(b)
            break
        except:
            print('Te pedí un número,no te hagas el gracioso')
        finally:
            print('Acá está la suma')
    
    return sumar

print(suma())

def division_cero():
    a = int(input('a:'))
    b = int(input('b:'))
    resultado = 0 #Se debe inicializar la variable a usar antes del método try.
    try:
        resultado = a / b 
    except ZeroDivisionError:
        print('Error! No se puede dividir por cero')
    
    return resultado
            
print(division_cero())