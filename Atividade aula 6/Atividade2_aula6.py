## DESAFIO 02

## Crie um programa que mostre na tela todos os números pares
## que estão no intervalo entre 1 e 50.




for n1 in range (0 , 51 , 1 ) :
    n2 = n1 % 2
    if n2 == 0 : 
        print (f"{n1}")
    