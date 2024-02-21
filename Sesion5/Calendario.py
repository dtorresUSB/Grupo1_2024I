meses=['Ene','Feb','Mar','Abr','May','Jun',
       'Jul','Ago','Sept','Oct','Nov','Dic']
dias=['31','29','31','30','31','30',
       '31','31','30','31','30','31']
festivo=['1 de enero y 6 de reyes','no hay','8 dia de la madre','30','31','30',
       '31','31','30','31','30','31']

n=input('Escriba las iniciales de un mes: ').capitalize()

for idx,mes in enumerate(meses):
    if mes==n:
        print(f'El mes {mes} tiene {dias[idx]} dias')
        print(f'festivos{festivo[idx]}')
