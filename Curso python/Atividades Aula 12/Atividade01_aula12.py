# DESAFIO 01

# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

n1 = int (input ("Digite a largura "))
n2 = int (input ("Digite o comprimento "))

def area (n1 , n2 ) : 
    area = n1 * n2
    return area

print (f"A area do terreno é igual a {area(n1 , n2 )}m³ .")