## DESAFIO 02

## Crie um programa que vai gerar cinco números aleatórios e colocar
## em uma tupla.

## Depois disso, mostre a listagem de números gerados e também
## indique o menor e o maior valor que estão na Tupla.


import random

# Gerar cinco números aleatórios e colocá-los em uma tupla  . comando tuple transformando os numeros randons em tupla , range 1 a 10 sao os numeros aleatorios , ultimo numero da sentença 5 = tanto de numeros aleatorios gerados 
numeros_aleatorios = tuple(random.sample(range(1, 10), 5))   # random.sample(): Esta função está sendo usada para selecionar aleatoriamente 5 elementos . 

# Mostrar a listagem dos números gerados
print("Números gerados:", numeros_aleatorios)

# Encontrar o menor e o maior valor na tupla
menor_valor = min(numeros_aleatorios)
maior_valor = max(numeros_aleatorios)

# Mostrar o menor e o maior valor
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor )
        