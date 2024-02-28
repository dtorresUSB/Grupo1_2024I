alumnos={'nombre':['Nicol','Johan','Catherin','David'],\
         'codigo':[12345,4567,2334,2345],\
            'carrera':'Ing. Mecatronica'}

print('Seccion de registro...')
cabecera=['nombre','codigo','carrera']
for idx, val in enumerate(alumnos):
    if val=='carrera':
        continue
    txt='Ingrese el' + cabecera[idx] +': '
    n=input(txt)
    alumnos[val].append(n)

for i in range(len(alumnos['nombre'])):
    print(f'Estudiante:{alumnos['nombre'][i]}\n'
      f'Codigo:{alumnos['codigo'][i]}\n'
      f'Carrera:{alumnos['carrera']}\n')

