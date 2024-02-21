
def main():
    milista=['hola',23,True,3.1416]
    print(len(milista))
    # idx=int(input('indice= '))
    # print(milista[idx])

    # for i in milista:
    #     print(i)

    for idx,elm in enumerate(milista):
        print(f'elemento #{idx}= {elm}')

if __name__=="__main__":
    main()