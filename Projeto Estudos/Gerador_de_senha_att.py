# Gerador de senha aleatória.



from random import randint , choice
import string
# Define todos os caracteres que podem ser usados na senha
caracteres = string.ascii_letters + string.digits

senha = []
n1 = int(input("Digite quantos dígitos você quer na senha (de 1 a 50): "))

for loop in range(n1):
    # Escolhe um caractere aleatório da lista de caracteres definida anteriormente
    char = choice(caracteres)
    senha.append(char)

# Concatena todos os elementos da lista senha em uma única string
senha_str = ''.join(senha)

print("Senha gerada:", senha_str)

#string: Aqui, string é o módulo embutido em Python que contém várias funções e constantes úteis para manipulação de strings.

# string.ascii_letters: string.ascii_letters é uma constante 
# neste módulo que representa todas as letras do alfabeto, tanto maiúsculas quanto minúsculas. Por exemplo, 
# inclui "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".
# string.digits: string.digits é outra constante neste módulo que representa todos os dígitos de 0 a 9.
# +: O operador + é usado para concatenar strings em Python. Quando usamos string.ascii_letters + string.digits, estamos 
# concatenando as strings que representam todas as letras do alfabeto (maiúsculas e minúsculas) com a string que representa 
# todos os dígitos.
# Então, em resumo, caracteres = string.ascii_letters + string.digits cria uma única string 
# contendo todas as letras maiúsculas, minúsculas e dígitos, que será usada para gerar as senhas.