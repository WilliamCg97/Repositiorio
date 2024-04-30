
from random import choice

#lista de opções para maquina 
lista = ["PEDRA" , "PAPEL"  , "TESOURA"]
valor = 0
vf = 3
# Sintaxe do codigo "Jogada maquina " 


while True : 

    jm = choice(lista) 

    n1= input("Informe sua escolha no jokenpo : ").upper()
    
   

    if jm == n1 :
        print(f"Ambos escolheram a mesma jogada {jm}, portanto impate !! ")
    
    elif  jm == "PEDRA" and n1 == "TESOURA":
        print(f"A maquina escolheu {jm}, portanto a maquina ganha !! :DD ")

    elif jm == "PEDRA" and n1 == "PAPEL" :
        print(f"A escolha da maquina foi {jm} , portanto você ganhou !! ")
        break
    
    elif jm == "TESOURA" and n1 == "PAPEL" :
        print(f" A escolha da maquina foi {jm}, portanto a maquina ganhou ")

    elif jm == "TESOURA" and n1 == "PEDRA" :
        print(f" A escolha da maquina foi {jm}, portanto você ganhou !!   ")
        break

    elif jm == "PAPEL" and n1== "TESOURA" :
        print(f" A escolha da maquina foi {jm}, você ganhou !!  ")
        break

    elif jm == "PAPEL" and n1 == "PEDRA" :

        print(f" A escolha da maquina foi {jm}, portanto a maquina ganhou !!")

    else : 
        print("opção incorreta ")
        continue 
valor = valor + vf
print("fim de jogo ")
print(f"Favor colocar mais uma ficha, Valor : R${valor}")