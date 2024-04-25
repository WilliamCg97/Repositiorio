# DESAFIO 03

# Faça um programa que tenha uma função chamada maior(), que
# receba três parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.
lista = [] 

# loop para pegar os 3 numeros que a pessoa digitar e colocalas em lista . 

for loop in range (0 , 3 , 1 ) : 
    n1 = int (input(f"Digite {loop + 1}º valor : "))
    lista.append(n1)

def maior(lista):
       
    maior_numero = lista[0]  #Deixando sempre o maior numero na parte 0 da lista 
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    
    return maior_numero

# Chama a função para encontrar o maior número na lista
resultado = maior(lista)
print (lista)
print (f"Maior numero é {  resultado }")