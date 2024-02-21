
def main():
    milista=[]
    n=input('Ingrese un elemento: ')
    milista.append(n)
    while n != 'salir':
        print(milista)
        milista.append(n)
        n=input('Ingrese un elemento: ')
        


if __name__=="__main__":
    main()