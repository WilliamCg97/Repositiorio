## DESAFIO 03

## Faça um programa que calcule a soma entre todos os números
## ímpares que são múltiplos de três e que se encontram no
## intervalo de 1 até 500.



for n1 in range (0 , 500 , 1 ) :
    n2 = n1 % 2
    n3 = n1 % 3
    n4 = n1 + n1 
    if n2 == 1 and  n3 == 0 :
    
        print(f"{n1} , a soma de todos os numeros impares é {n4}")
    