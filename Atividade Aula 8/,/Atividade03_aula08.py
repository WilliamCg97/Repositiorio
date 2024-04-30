## DESAFIO 03

## Crie um programa que leia vários números inteiros pelo
## teclado. No final da execução, mostre a média entre todos os
## valores e qual foi o maior e o menor valores lidos. O programa
## deve perguntar ao usuário se ele quer ou não continuar a
## digitar valores

n = 1 
soma = 0
rodadas = 0 
n2 = "N" 
while True :
        
      
    n1 = int(input(" numero : "))
          
    soma = soma + n1 
    rodadas = rodadas + 1 
    
    
    if n2 == "N" : 
        
        n2 = input("deseja encerrar o  programa digitando  s // n  :").upper() 

        
        
    
    elif n2 == "S" : 
        media = soma / rodadas 
        print(f"A media dos numeros é {media}")
        print(f"A soma dos numeros é {soma}")
        break




