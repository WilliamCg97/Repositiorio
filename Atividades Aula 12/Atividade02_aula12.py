# DESAFIO 02

# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.

# Ex:

# escreva(‘Olá, mundo!!’)

# Saída

# -----------------------------------

#         Olá, mundo
        
# -----------------------------------

def escreva(texto):
    tamanho_linha = len(texto) + 4
    print('-' * tamanho_linha)
    print(f'  {texto}')
    print('-' * tamanho_linha)

# Teste
escreva('Olá, mundo!:D :D :D !')