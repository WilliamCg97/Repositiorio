## Esplicação sobre bibliotécas 
## Random = puxa numeros aléatórios. 
## from random import randint : nesse caso estou somente importando o comando randint. 
## o comando " as " seria para renomear a biblioteca. como no exemplo.
## Utilizando o " * " ele importa todos os comandos da biblioteca. 



import random


n1 = random.randint( 0,10 )
n2 = random.randint( 0,10 )
media = (n1 + n2) / 2 

print(f"nota da primeira prova {n1}")
print(f"nota da segunda prova {n2}")

if media >= 7 :
    print("Aluno aprovado :D !! ")

else:
    print("Aluno reprovado :( " )
    
    
    