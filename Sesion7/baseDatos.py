personas={}
for i in range(3):
    n=input('Ingrese el nombre: ')
    if 'nombre' in personas: #Si hay datos
        personas['nombre'].append(n)
        print(personas)
    else:               #Si no hay datos
        personas['nombre']=[n]