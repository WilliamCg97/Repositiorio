# DESAFIO 03

# Escreva um programa que solicite ao usuário para digitar um
# número inteiro e exiba o resultado da sua raiz quadrada. Lide
# com o erro caso o número seja negativo.

from math import sqrt 


try : 
    n1 = int (input("Digite um valor : "))
    raiz = sqrt(n1)
    
except ValueError:
    print ("Digite um valor numero por favor ") 
    
else : 
    print (raiz)
     
