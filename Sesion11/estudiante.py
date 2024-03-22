
class Estudiante:
    def __init__(self):
        self.nombre="Juan"
        self.codigo=None
        self.carrera=None
        self.universidad=None

    def hablar(self):
        print(f'mi nombre es {self.nombre}')

        
def main():
    est1=Estudiante()
    est1.nombre="Falcao Garcia"
    est1.codigo=23243543
    est1.carrera="Deportes"
    est1.universidad="La Salle"
    print(f'El estudiante {est1.nombre}, de codigo {est1.codigo},\n'
          f'se encuentra en la u {est1.universidad} estudiando {est1.carrera}')
    
    
    est2=Estudiante()
    est2.nombre="Jhonny Bravo"
    est2.codigo=345435
    est2.carrera="Derecho"
    est2.universidad="Javeriana"
    print(f'El estudiante {est2.nombre}, de codigo {est2.codigo},\n'
          f'se encuentra en la u {est2.universidad} estudiando {est2.carrera}')
    print('---------------------------------------------------------------------------')
    print(id(est1))
    print(id(est2))
    est3=Estudiante()
    print(id(est3))
    print('---------------------------------------------------------------------------')
    est1.hablar()
    est2.hablar()
    est3.hablar()



if __name__=="__main__":
    main()