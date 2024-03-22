class Estudiante:
    #--------------Constructor---------------
    def __init__(self):
        self.__nombre=None
        self.__codigo=None
        self.carrera=None
        self.universidad=None
        self.autenticacion=False

    #--------------Setters-------------------
    def setNombre(self,nombre:str):
        if nombre=='':
            print('Error en los datos')
        else:
            self.__nombre=nombre
            self.autenticacion=True
    
    def setCodigo(self,codigo:int):
        print(type(codigo))
        self.__codigo=codigo

    #--------------Getters-------------------
    def getNombre(self):
        if self.autenticacion==True:
          return self.__nombre
        else:
          print('error al retorno de datos')
    
    
    def getCodigo(self):
        return self.__codigo

    #--------------Metodos-------------------
    def hablar(self):
        print(f'mi nombre es {self.nombre}')

        
def main():
    est1=Estudiante()
    est1.setNombre(input('Ingrese su nombre: '))
    print(f'mi nombre es {est1.getNombre()}')
    est1.setCodigo(input('Ingrese su codigo: '))
    print(f'mi codigo es {est1.getCodigo()}')

    est2=Estudiante()
    # print(f'El estudiante {est1.nombre}, de codigo {est1.codigo},\n'
    #       f'se encuentra en la u {est1.universidad} estudiando {est1.carrera}')

if __name__=="__main__":
    main()


