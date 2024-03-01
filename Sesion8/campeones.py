
def datosDB(f):
    lectura=f.readlines()
    datos=[]
    for i in lectura:
        datos.append(i.rstrip('\n').split(','))
    return datos

def campeones(datos):
    campeon=[]
    for campeones in datos:
        if campeones[12]=='Final':
            if campeones[2]>campeones[4] or campeones[3]>campeones[5]:
                print(campeones[0])
            elif campeones[2]<campeones[4] or campeones[3]<campeones[5]:
                print(campeones[1])
            #campeon.append(campeones)

    print(datos[1][12])
    print(len(datos[1]))

if __name__=="__main__":
    f=open('wcm.csv','r',encoding="utf8")     #Crear un objeto de lectura
    DB=datosDB(f)          #Formateo
    campeones(DB)