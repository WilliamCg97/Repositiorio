## Atividade ! 
## 1 : Escreva um programa que faça o computador “pensar” em um
## número inteiro entre 5 e 0 e peça para o usuário tentar descobrir
## qual foi o número escolhido pelo computador.


import random

n1= int(input("Escolha um numero de 0 a 5."))
n2= random.randint( 0,5 )
 
if n2 == n1 :
    print("Voce acertou o numero que a maquina escolheu !!! :D ")
    
else :
    
    print(f"A maquina escolheu {n2}")
    print(" Você errou o numero :D  ! ")
        
    
    