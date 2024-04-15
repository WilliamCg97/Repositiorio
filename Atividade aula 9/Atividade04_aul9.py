## DESAFIO 04

## Desenvolva um programa que leia quatro valores pelo teclado e
## guarde-os em uma tupla. No final, mostre:

#3 A) Quantas vezes apareceu o valor 9.   # .count  "conta entre todos  itens da lista " . index "mostra somente o primeiro item da lista "

#3 B) Em que posição foi digitado o primeiro valor 3. 

#3 C) Quais foram o números pares.


lista = [] 
valor_nove = 0
numeros_pares = []
loc_trez = []




for loop in range (0,4) :
    n1 =int(input("Digite 4 numeros : "))
    lista.append(n1)
    par = n1 % 2 
    
    
    ## C) Quais foram o números pares.
    if par == 0 : 
        numeros_pares.append(n1)

    if n1 == 3 :
        loc_trez.append(loop)
    ## tambem pode ser feito utilizando o comando tupla.count ()= " tupla é minha variavel "  .count comando  
    if n1 == 9 : 
        valor_nove +=1  


## Convertendo as listas em tuplas      
t3=tuple(loc_trez)
tupla = tuple(lista) 
tp = tuple(numeros_pares)

print (f"{tupla}")
print(f"os numeros pares sao {tp}")
print(f"O valor 3 foi colocado na posição {t3}")
print(f"foi colocado o numero -9- {valor_nove} vezes ")


##Segunda Maneira
#numeros = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),\
#int(input('Digite um número: ')),int(input('Digite um número: ')))
#
#


