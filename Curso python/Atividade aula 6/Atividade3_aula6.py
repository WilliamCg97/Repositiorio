## DESAFIO 03

## Faça um programa que calcule a soma entre todos os números
## ímpares que são múltiplos de três e que se encontram no
## intervalo de 1 até 500.

soma=0

for n1 in range (1 , 500 , 1 ) :
    n2 = n1 % 2
    n3 = n1 % 3
    n4 = n1 + n1 
    if n2 == 0 and  n3 == 1 :
        
        print(f" A soma de todos os numeros impares é {n4}")
    