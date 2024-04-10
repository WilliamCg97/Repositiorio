# DESAFIO 02

# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final serão
# exibidos todos os valores únicos digitados, em ordem
# crescente.

lista=[]
n2= 0

while True : 
    
    n1 = int(input("Digite o numero que deseja cadastrar "))
    lista.append(n1)
    n2 +=1 
    validando= lista.index{n1}
    
    if validando == 2 :
        print ("numero ja cadastrado") 
        
