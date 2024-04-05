## DESAFIO 02

## Crie um programa que leia vários números inteiros pelo
## teclado. O programa só vai parar quando o usuário digitar o
## valor 999, que é a condição de parada. No final, mostre
## quantos números foram digitados e qual foi a soma entre eles
## (desconsiderando o 999).



print (" Condição para termino do programa é digitar 999 ")

n2 = 999
soma = 0 

while True : 
        
    n1 = int (input("Digite um numero inteiro : ") )
    if n1 != n2 :
        soma = soma + n1
        
        print (f"{n1}" , end= "-" ) 
        
         
    else  :
        print(f"{soma}")
        
        break
    
    
        
              