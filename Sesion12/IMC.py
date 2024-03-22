
class Persona:
    #--------------Constructor-------------------
    def __init__(self):
        self.__nombre=None
        self.__estatura=None
        self.__peso=None
        self.__edad=None
        self.__genero=None
    
    #--------------Setters-------------------
    def setNombre(self,nombre):
        self.__nombre=nombre

    def setEstatura(self,estatura:int):
        while estatura<0:
            print('La estatura no puede ser menor a cero')
            estatura=int(input('Ingrese su estatura: '))
        self.__estatura=estatura

    def setPeso(self,peso:int):
        while peso<0:
            print('el peso no puede ser menor a cero')
            peso=int(input('Ingrese el peso: '))
        self.__peso=peso

    def setEdad(self,edad:int):
        self.__edad=edad

    def setGenero(self,genero:int):
        self.__genero=genero
        
    #--------------Getters-------------------
    def getNombre(self):
        return self.__nombre
    
    def getEstatura(self):
        return self.__estatura
    
    def getPeso(self):
        return self.__peso

    def getEdad(self):
        return self.__edad

    def getGenero(self):
        return self.__genero

    #--------------Metodos-------------------
    def IMC(self):
        IMC=self.getPeso()/((self.getEstatura()/100)**2)
        return IMC


def main():
    cliente1=Persona()
    cliente1.setNombre(input('Ingrese su nombre: '))
    cliente1.setEstatura(int(input('Ingrese su estatura: ')))
    cliente1.setPeso(int(input('Ingrese su peso: ')))
    print(cliente1.IMC())


if __name__=="__main__":
    main()