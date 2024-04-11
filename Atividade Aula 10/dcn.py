estado = {}
brasil = list()

for c in range (0,2 ):
    estado['uf'] = str(input("Unidade federativa"))
    estado ['sigla']= str(input("Sigla do estado"))
    brasil.append(estado.copy())
    
print(estado)