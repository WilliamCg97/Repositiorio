## DESAFIO 06

## Crie um programa que faça o computador jogar Jokenpô com
## você:
## petra papel tesoura . 



## explicaç~ão 
## utilizar " from random import choice  "

from random import choice

#lista de opções para maquina 
lista = ["PEDRA" , "PAPEL"  , "TESOURA"]

# Sintaxe do codigo "Jogada maquina " 
jm = choice(lista) 


n1= input("Informe sua escolha no jokenpo : ").upper()


if jm == n1 :
    print(f"Ambos escolheram a mesma jogada {jm}, portanto impate !! ")
    
elif  jm == "PEDRA" and n1 == "TESOURA":
    print(f"A maquina escolheu {jm}, portanto ela ganha !! :DD ")

elif jm == "PEDRA" and n1 == "PAPEL" :
    print(f"A escolha da maquina foi {jm} , portanto voce ganhou !! ")
    
elif jm == "TESOURA" and n1 == "PAPEL" :
    print(f" A escolha da maquina foi {jm}, portanto a maquina ganhou ")

elif jm == "TESOURA" and n1 == "PEDRA" :
    print(f" A escolha da maquina foi {jm}, portanto você ganhou !!   ")

elif jm == "PAPEL" and n1== "TESOURA" :
    print(f" A escolha da maquina foi {jm}, você ganhou !!  ")

else:
    print(f" A escolha da maquina foi {jm}, portanto a maquina ganhou !!")
    
    
    