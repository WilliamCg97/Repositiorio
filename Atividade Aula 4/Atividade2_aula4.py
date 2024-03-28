## Atividade 2 
## DESAFIO 02  Escreva um programa que leia a velocidade de um carro.
## Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
## ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

n1 = int(input("Digite a velocidade do carro ."))
n2 = 80 
fmulta = (n1 - 80) * 7 


if n1<=80 :
    print("Voce esta dentro do parametro de velocidade da via !! parabens :D ")
    
else : 
    print(f"voce ultrapassou o limite da via. multa referente ao acontecido R${fmulta}")
   
