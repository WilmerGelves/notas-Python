#Clases

class auto:
    def __init__(self,marca:str,caballos:int,color:str):
        self.marca = marca
        self.caballos = caballos
        self.color = color

    def mostrarC(self):
        print('El carro {} tiene {} caballos de fuerza y es de color {}'.format(self.marca, self.caballos,self.color))


carro1 = auto('Audi',120,'amarillo')
carro1.mostrarC()