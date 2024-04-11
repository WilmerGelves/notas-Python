#Ejercicio Notas
import os
if __name__ == "__main__":
    parciales = 0.0 
    trabajos = 0.0
    quizes = 0.0
    nombreAlumno = ''

    nombreAlumno = str(input('Ingrese el nombre del alumno:'))
    os.system('cls')
    for i in range(0,3,1):
        parciales += float(input(f"Ingrese el parcial Nro {i+1}: "))
        os.system('cls')
    parciales = (parciales/3)*0.6
    
    for i in range(0,4,1):
        quizes += float(input(f"Ingrese el quiz Nro {i+1}: "))
        os.system('cls')
    quizes = (quizes/4)*0.25

    for i in range(0,2,1):
        trabajos += float(input(f"Ingrese el trabajo Nro {i+1}: "))
        os.system('cls')
    trabajos = (trabajos/3)*0.15

    notaFinal = (parciales + trabajos + quizes)
    if(notaFinal >=1.0) and (notaFinal < 3.0):
        print(f'El alumno {nombreAlumno} reprobó la materia con una nota de {notaFinal}') 
    elif(notaFinal >= 3.0) and (notaFinal < 4.0):
        print(f'El alumno {nombreAlumno} aprobó la materia con una nota de {notaFinal}') 
    elif(notaFinal >= 4.0) and (notaFinal <= 5.0):
        print(f'El alumno {nombreAlumno} aprobó la materia con una nota de {notaFinal}') 
    else:
        print('Verifique los datos ingresados')
