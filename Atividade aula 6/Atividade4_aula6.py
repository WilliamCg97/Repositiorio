## DESAFIO 04

## Refaça o DESAFIO 09, mostrando a tabuada de um número
## que o usuário escolher, só que agora utilizando um laço for.



n1= int(input("Qual tabuada deseja saber ? ")) 

for n2 in range (0 , 21 , 1 ) : 
    n3 = n2 * n1 

    if n2 <= 20 :
        print (f"{n1} X {n2} = {n3}")
        
   