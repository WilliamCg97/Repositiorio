# DESAFIO 06

# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final mostre os
# valores pares e impares e ordem crescente.




lista = [] 
lista2= []
lista3= [] 


for loop in range (7,1) : 
    n1 = int(input("Digite um valor : "))
   
    validar = n1 % 2    
    
    if validar == 0:
        lista2.append(n1)
        lista.append(n1)

    elif validar == 1:
        lista3.append(n1)
        lista.append(n1) 
        
        