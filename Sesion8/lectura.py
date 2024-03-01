
def wholeFile(f):
    A=f.read().split('\n')
    B=[]
    for i in A:
        B.append(i.split(','))
    print(B)
    print(B[0][2])
    return B

def oneLine(f):
    A=f.readline().rstrip('\n').split(',')
    B=[]
    while A!=['']:
        B.append(A)
        A=f.readline().rstrip('\n').split(',')
    print(B)
    print(B[2][2])
    return B

def listFile(f):
    A=f.readlines()
    print(A)
    B=[]
    for i in A:
        B.append(i.rstrip('\n').split(','))
    print(B)
    print(B[1][3])
    return(B)

if __name__=="__main__":
    f=open('matrizAsignacion.txt','rt')     #Crear un objeto de lectura
    #A=wholeFile(f)
    #A=oneLine(f)
    A=listFile(f)
    print(type(A))
    #f.seek(11)     ubicar el puntero