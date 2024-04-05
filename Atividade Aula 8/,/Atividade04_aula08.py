## DESAFIO 04

## Faça um programa que jogue par ou impar com o computador.
## O jogo só será interrompido quando o jogador perder,
## mostrando o total de vitorias consecutivas que ele conquistou
## no final do jogo.

from random import randint

lista=["IMPAR" , "PAR"]
ponto = 0




while True: 
    n2= randint( 0,10 )     
    t1 = input (" Escolha impar ou par ").upper()
    
   
    if t1 == "PAR" :
         maquina = "IMPAR"
         
    else :
        maquina = "PAR"     
            
          
    n1 =  int(input("Digite um numero : ")) 
    
    rodada = n1 + n2  
    resultado = rodada % 2
    
    ## par 
    if resultado == 0  and t1 == "PAR" :
        print (f"A maquina escolheu {n2}")
        print("Portanto PAR ganhou !! ")  
        ponto= ponto+1
        print(f"Você ganhou to {ponto}")
    
    elif  resultado == 1  and t1 == "PAR" :
        print (f"A maquina escolheu {n2}")
        print ("portanto a maquina  ganhou ")        
        print(f"{ponto}")
        break
        
    
     
    if resultado == 0  and t1 == "IMPAR" :
        print (f"A maquina escolheu {n2}")
        print("Portanto maquina ganhou !! ")
        print(f"{ponto}")
        break  
    
    elif  resultado == 1  and t1 == "IMPAR" :
        print (f"A maquina escolheu {n2}")
        print ("portanto você  ganhou ")        
        ponto = ponto+ 1 
        print(f"Voce ganhou um ponto {ponto}")
        

    
              
        






