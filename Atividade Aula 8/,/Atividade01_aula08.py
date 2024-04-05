##DESAFIO 01

## Faça um jogo, onde o computador vai “pensar” em um número
## entre 0 a 10. Só que agora o jogador vai tentar adivinhar até
## acertar, mostrando no final quantos palpites foram necessários
## para vencer.
 


    
from random import randint



n1 = int(input(" Escolha o numero  : "))
n2= randint( 0,10 )
n3 = 1

while True :  
    
    n1 = int(input(" Escolha o numero : "))
    
    if n1 != n2 :
        n3  = n3 + 1 
    
        
    else : 
        n3  = n3 + 1
        print(" Você acertou o numero !! :D ")
        print(f"o numero de tentativas foi {n3} ")
        break



