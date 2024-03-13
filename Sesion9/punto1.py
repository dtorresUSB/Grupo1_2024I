
def contador_de_letras():
    txt=input('ingrese una frase: ').lower()

    conteo={}
    for i in txt:
        if i ==' ':
            i='space key'
        if i not in conteo:
            conteo[i]=1
        else:
            conteo[i]+=1
    print(conteo)

    for key in conteo:
        print(f'letra {key}: aparece {conteo[key]} veces')


if __name__=="__main__":
    contador_de_letras()