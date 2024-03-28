## Atividade 4 
## Faça um programa que leia três números e mostre qual é o
## maior e qual é o menor.
## and -- or  

n1= int(input("Digite um numero de 1 a 10 : "))
n2= int(input("Digite um numero de 1 a 10 : "))
n3= int(input("Digite um numero de 1 a 10 : "))

if n1 > n2 and n1 > n3 :
    
    print(f"maior numero é o {n1}")
 

if n2 > n1 and n2 > n3 :
    
    print(f"O maior numero é {n2}")


if  n3 > n2 and n3 > n1 : 

    print(f"o mairo numero é o {n3}")


## 

if n1 < n2 and n1 < n3 :
    
    print(f" O menor numero é {n1}")
 

if n2 < n1 and n2 < n3 :
    
    print(f"O menor numero é {n2}")


if  n3 < n2 and n3 < n1 : 

    print(f"O menor numero é {n3}")
