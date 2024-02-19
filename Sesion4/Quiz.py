def tabulacion(n):
    
    txt=''
    for i in range(n):
        fx=3*i+5
        txt+=' '+str(fx)
    print(txt)
    print(f'nombre2:{__name__}')

if __name__=="__main__":
    tabulacion(20)