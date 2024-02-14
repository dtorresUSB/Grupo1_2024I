a=float(input('Ingrese valor de a: '))
b=float(input('Ingrese valor de b: '))
c=float(input('Ingrese valor de c: '))

raiz=((b**2)-4*a*c)
print(raiz)
if raiz>0:
    x1=(-b+raiz**(1/2))/(2*a)
    x2=(-b-raiz**(1/2))/(2*a)
    print(f'las raices reales son {x1} y {x2}')
else:
    print('Las raices son imaginarias')