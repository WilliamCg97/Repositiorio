#CRIANDO UM DICIONÁRIO DO ZERO usando lista
estado ={}
brasil = list()


for c in range(0,2):
    estado['uf']= str(input('Unidade federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil.append(estado.copy())


print(estado)  


print(brasil)


print('******************')


for e in brasil: # percorrer cada dicionario
    for v in e.values(): # exibir cada valor
        print(v, end=' ')
    print(' ')