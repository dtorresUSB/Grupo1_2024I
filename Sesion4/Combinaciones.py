from factorial import fcn_factorial as f

def main():
    n=int(input('Ingrese el numero de elementos: '))
    m=int(input('Ingrese el numero de grupos: '))

    comb= f(n)/(f(m)*f(n-m))
    print(f'Numero de combinaciones: {comb}')



if __name__=="__main__":
    main()