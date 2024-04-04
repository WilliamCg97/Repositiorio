## DESAFIO 05

## Desenvolva um programa que leia seis números inteiros e
## mostre a soma apenas daqueles que forem pares. Se o valor
## digitado for impar desconsidere-o.

total = 0 

for loop in range (1,7) : 
    n1 = int ( input (f" Escolha um numero {loop} s"))
    resto = n1 % 2 
    
    if resto  == 0 :
        total = total + n1 
    else : 
        print (f"{total + n1 }")