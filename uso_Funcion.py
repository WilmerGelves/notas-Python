import os
def calculadora(valorA : int, valorB : int,op : str):
    resultado = 0 
    match op:
        case '+':
            resultado = valorA + valorB
        case '-':
            resultado = valorA - valorB
        case '*':
            resultado = valorA * valorB
        case '/':
            resultado = valorA / valorB
        case _ :
            return 'Opss. Operacion no existe '
    return resultado
    os.system('pause')
if __name__== '__main__':
    opcion = 1
    titulo = """
    ***************************
    * Operaciones matemáticas *
    ***************************
    """
    while (opcion <5):
        os.system('cls')
        print(titulo)
        menu = '\t1. Suma \n\t2.Resta \n\t3.Multiplicacion \n\t4.Division \n\t5.Salir'
        print(menu)
        opcion = int(input('\t:=>'))
        os.system('cls')
        match opcion:
            case 1:
                nextCal = True
                while (nextCal):
                    valorA = int(input('Primer número: '))
                    valorB = int(input('Segundo Número: '))
                    print('El resultado de la suma es: ',calculadora(valorA, valorB,'+')) 
                    nextCal = bool(input('Desea realizar otra suma S(si) o Enter(no)'))
                    os.system('cls')
            case 2:
                nextCal = True
                while (nextCal):
                    valorA = int(input('Primer número: '))
                    valorB = int(input('Segundo Número: '))
                    print('El resultado de la resta es: ',calculadora(valorA, valorB,'-') )
                    nextCal = bool(input('Desea realizar otra suma S(si) o Enter(no)'))
                    os.system('cls')
            case 3: 
                nextCal = True
                while (nextCal):
                    valorA = int(input('Primer número: '))
                    valorB = int(input('Segundo Número: '))
                    print('El resultado de la multiplicación es: ',calculadora(valorA, valorB,'*')) 
                    nextCal = bool(input('Desea realizar otra suma S(si) o Enter(no)'))
                    os.system('cls')
            case 4: 
                nextCal = True
                while (nextCal):
                    valorA = int(input('Primer número: '))
                    valorB = int(input('Segundo Número: '))
                    print('El resultado de la división es ',calculadora(valorA, valorB,'/'))
                    nextCal = bool(input('Desea realizar otra suma S(si) o Enter(no)'))
                    os.system('cls')
            case 5: 
                print('Vuelva pronto')
                os.system('pause')
            case _:
                print('Opss... La opción no es válida')
                opcion = 0
                os.system('pause')

