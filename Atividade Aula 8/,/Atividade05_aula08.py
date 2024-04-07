## DESAFIO 05

## Crie um programa que leia a idade e o sexo de varias
## pessoas. A cada pessoa cadastrada, o programa deverá
## perguntar se o usuário quer ou não continuar. No final, mostre:

## A) Quantas pessoas tem mais de 18 anos.

## B) Quantos homens foram cadastrados.

## C) Quantas mulheres tem menos de 20 anos.

p_cadastro = 0
h_cadastro = 0 
m_m_vinte = 0


while True :

    n1 = input("Digite seu sexo, F para feminino e M para masculino : ").upper()
    n2 = int(input ("Digite sua idade : "))

    if n2 > 18:
        p_cadastro += 1

    elif n1 == "M" :
        h_cadastro += 1

    elif n1 == "F" and n2 <= 20 :
        m_m_vinte += 1  

    continuar = input("Deseja cadastrar mais uma pessoa? (S/N): ").upper()

    if continuar != "S":
        break

print (f"Foram cadastradas {p_cadastro} Acima de 18 anos ")
print (f"Foram cadastrados {h_cadastro} homens ")
print (f"Foram cadastradas {m_m_vinte} mulheres com menos de 20 anos.")







        
    