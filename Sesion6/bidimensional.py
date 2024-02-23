from random import randint as r

def main():
    rows=int(input('Ingrese el numero de filas: '))
    cols=int(input('Ingrese el numero de columnas: '))
    matriz=[]
    for i in range(rows):
        matriz.append([])
        for j in range(cols):
            n=r(0,100)
            matriz[i].append(n)
    print(matriz)
    print(f'posición (1,1): {matriz[1][1]}')

    for i in matriz:
        print(i)



if __name__=="__main__":
    main()