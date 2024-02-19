#------------- Funcion con parametros --------------
def operaciones(a,b):
    c=a+b
    d=a-b
    return c,d

#------------- Funcion sin parametros --------------
def imprimir():
    print('\nOperacion exitosa: ')


n1=int(input('Ingrese un numero: '))
n2=int(input('Ingrese un numero: '))
imprimir()
sumar,restar=operaciones(n1,n2)
print(f'suma:{sumar}, resta:{restar}')