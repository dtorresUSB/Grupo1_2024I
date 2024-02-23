import random as rand

def main():
    lista=[]
    decimales=[]
    ahorcado=[]
    word="esternocleidomastoideo"
    for i in range(10):
        n=rand.randint(0,10)
        d=round(rand.uniform(0,10),2)
        p=rand.choice(word)
        ahorcado.append(p)
        decimales.append(d)
        lista.append(n)
    # print(lista)
    # print(decimales)
    # print(ahorcado)
    return lista,decimales,ahorcado

def sliding(listados):
    print('--------------Imprimiendo listados----------------')
    for i in listados:    #listados=([lista],[decimales],[ahorcado])
        print(i)

    print('--------------recorriendo listas----------------')
    for idx,val in enumerate(listados[1]):
        print(f'indice:{idx} - valor:{val}')


if __name__=="__main__":
    listados=main()
    sliding(listados)
