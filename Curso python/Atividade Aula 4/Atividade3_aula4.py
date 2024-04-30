##Desenvolva um programa que pergunte a distância de uma
## viagem em Km. Calcule o preço da passagem cobrando R$
## 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
## viagens mais longas.

n1 = int(input("Qual a distancia da cidade que você deseja ir ? digite valor em km "))
dm= 200

## até 200 km
c1 = (0.50 * n1 )
## Acima de 200 km 
c2 = (0.45 * n1 )


if n1 <= dm : 
    print(f"Valor da viagem R${c1}")

else :
    print(f"Valor da viagem é R${c2}")