## DESAFIO 03

## Crie um programa que leia vários números inteiros pelo
## teclado. No final da execução, mostre a média entre todos os
## valores e qual foi o maior e o menor valores lidos. O programa
## deve perguntar ao usuário se ele quer ou não continuar a
## digitar valores

n = 1 
soma = 0
rodadas = 0 

while True :
    
    
    
    n1 = int(input(" numero : "))
    
    soma = soma + n1 
    rodadas = rodadas + 1 
    
          
    
    if n == "N" : 
        
        n1 = int(input(" numero : "))
        n2 = input("deseja encerrar o  programa digitando  s // n  :").upper() 

        
        
    
    else : 
        media = soma / rodadas 
        print(f"{media}")
        print(f"{soma}")
        break


