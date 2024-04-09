## DESAFIO 04

## Desenvolva um programa que leia quatro valores pelo teclado e
## guarde-os em uma tupla. No final, mostre:

#3 A) Quantas vezes apareceu o valor 9.   # .count  "conta entre todos  itens da lista " . index "mostra somente o primeiro item da lista "

#3 B) Em que posição foi digitado o primeiro valor 3. 

#3 C) Quais foram o números pares.


lista = [] 
valor_nove = 0




for loop in range (0,4) :
    n1 =int(input("Digite 4 numeros : "))
    lista.append(n1)
    
tupla = tuple(lista) 


## valor 9 
valor9 = tupla.count(9)
print (valor9)

#valor 3 
valor3 = tupla.index(3)
print (valor3)

par = tupla % 2 



