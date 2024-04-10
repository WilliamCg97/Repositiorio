##DESAFIO 01

# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.

##No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.


lista =[]


for loop in range (0 , 5) : 
    n1 = int(input("Digite 5 valores : "))
    lista.append(n1)
    mlista = min(lista)
    mmlista = max(lista)

print (lista )
print (mlista) 
print (mmlista) 
