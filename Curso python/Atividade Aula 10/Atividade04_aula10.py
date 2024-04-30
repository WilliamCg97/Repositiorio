##DESAFIO 04

# Crie um programa que vai ler vários números e colocar em
# uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.


lista = [] 
lista2= []
lista3= [] 


while True :
    n1 = int(input("Digite um valor : / digite 0 para encerrar o programa / "))
    if n1 == 0 : 
        print (f"Lista de numeros impares : {lista3}")
        print (f"Lista de numeros pares : {lista2}")
        print (f"Lista de numeros digitados : {lista}")
        break
    
    
    validar = n1 % 2 
       
    
    if validar == 0:
        lista2.append(n1)
        lista.append(n1)

    elif validar == 1:
        lista3.append(n1)
        lista.append(n1)    