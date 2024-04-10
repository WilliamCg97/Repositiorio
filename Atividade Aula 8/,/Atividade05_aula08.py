## DESAFIO 05

## Crie um programa que leia a idade e o sexo de varias
## pessoas. A cada pessoa cadastrada, o programa deverá
## perguntar se o usuário quer ou não continuar. No final, mostre:

## A) Quantas pessoas tem mais de 18 anos.

## B) Quantos homens foram cadastrados.

## C) Quantas mulheres tem menos de 20 anos.



pessoas_mais_de_18 = 0
homens_cadastrados = 0
mulheres_menos_de_20 = 0

while True:
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
       
    if sexo != "M" or sexo != "F" :
        print("Digite uma letra valida")
        continue
    
    idade = int(input("Digite a idade da pessoa: "))  
        
    if idade > 18:
        pessoas_mais_de_18 += 1

    if sexo == 'M':
        homens_cadastrados += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1

    continuar = input("Deseja cadastrar outra pessoa? (S/N): ").upper()
    if continuar != 'S':
        break

print(f"A) Quantidade de pessoas com mais de 18 anos: {pessoas_mais_de_18}")
print(f"B) Quantidade de homens cadastrados: {homens_cadastrados}")
print(f"C) Quantidade de mulheres com menos de 20 anos: {mulheres_menos_de_20}")