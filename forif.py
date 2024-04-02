
from  random import randint


maquina = 0 
usuario = 0



# inicio fim salto     i  f s
for elemento in range (1,11,1) : 
    aleatorio = randint(0,5)
    
    n1= int(input(f"Rodada -{elemento}   Digite um numero : "))

    if n1 == aleatorio :
        print("Você Acertou")
        usuario = usuario +1
         
    else : 
        print("VocÊ errou ! ")
        maquina = maquina + 1 
        