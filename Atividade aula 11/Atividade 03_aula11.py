# DESAFIO 03

# Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-os (com idade) em um
# dicionário se por acaso o CTPS for diferente de ZERO, o
# dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a
# pessoa vai se aposentar.

# Sabendo que ele vai se aposentar após 35 anos de
# colaboração.
from datetime import date

anoatual= date.today().year


dcn = {
    'nome': str(input("Nome :")),
    'Ano de nascimento ' : int(input("Ano de nascimento")) ,
    'Carteira de trabalho ' : int(input("Cartei de trabalho : (0 se nao tem )"))
        }
print (dcn)
idade = anoatual - dcn['Ano de nascimento']
del dcn ['Ano de nascimento']
dcn['idade'] = idade

if dcn ['Carteira de trabalho '] == 0 : 
    for k , v in dcn.items() :
    