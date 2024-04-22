# DESAFIO 01

# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.


def Area (largura , comprimento ) : 
    area1 = largura * comprimento
    return area1

n1 = int (input ("Digite a largura "))
n2 = int (input ("Digite o comprimento "))
print (Area (n1,n2 ))