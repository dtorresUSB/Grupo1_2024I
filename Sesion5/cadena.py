word=input('Ingrese una frase: ')
idx=int(input('Que posición desea conocer: '))
print(f'elemento: {word[idx]}')
print(f'Longitud de la frase: {len(word)}')

for i in range(len(word)):
    print(word[i])