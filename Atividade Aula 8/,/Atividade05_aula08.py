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


<<<<<<< HEAD
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







        
    
=======
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
>>>>>>> fa2063ff16f3f53451bd7273fc412e3e940877d5
