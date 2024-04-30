## DESAFIO 06

## Desenvolva um programa que leia o primeiro termo e a razão
## de uma PA. No final, mostre os 10 primeiros termos dessa
## progressão.

## progreçao aritimetica //  

## usuario digitando o termo ex (termo = 15 ) razao = 10 resultado seria , 25 35 45 55 65 75 ... 


## n1 termo 
## n2 razão 

 
n1 = int(input("Digite o termo : "))
n2 = int(input("Digite a razao : "))
ultimotermo = (n1 + (10 - 1 ) * n2 ) + n2


for loop in range (n1, ultimotermo ,n2) : 
    print(f"{loop}", end= ' -> ')
else : 
    print("fim ")




