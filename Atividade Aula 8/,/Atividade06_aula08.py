## DESAFIO 06

## Crie um programa que leia o nome e o preço de vários
## produtos. O programa deverá perguntar se o usuário vai
## continuar. No final, mostre:

# A) Qual é o total gasto na compra.

# B) Quantos produtos custam mais de R$ 100,00.

# C) Qual é o nome do produto mais barato.



total_spent = 0  # Total gasto na compra
products_over_100 = 0  # Contador de produtos que custam mais de R$ 100.00
cheapest_product = None  # Nome do produto mais barato
cheapest_price = None  # Preço do produto mais barato

# Loop infinito até o usuário decidir parar
while True:
    # Solicitando ao usuário para inserir o nome e o preço do produto
    product_name = input("Digite o nome do produto: ")
    product_price = float(input("Digite o preço do produto: "))

    # Adicionando o preço do produto ao total gasto
    total_spent += product_price

    # Verificando se o preço do produto é maior que R$ 100.00
    if product_price > 100:
        # Se for, incrementa o contador
        products_over_100 += 1

    # Verificando se este é o primeiro produto ou se o preço do produto é menor que o preço mais barato já registrado
    if cheapest_price is None or product_price < cheapest_price:
        # Se for, atualiza o preço mais barato e o nome do produto mais barato
        cheapest_price = product_price
        cheapest_product = product_name

    # Perguntando ao usuário se ele quer continuar
    continue_choice = input("Você quer continuar? (S/N) ")
    # Se a resposta não for 's', sai do loop
    if continue_choice.lower() != 's':
        break

# Imprimindo os resultados
print(f"A) O total gasto na compra é R$ {total_spent}")
print(f"B) {products_over_100} produtos custam mais de R$ 100.00")
print(f"C) O nome do produto mais barato é {cheapest_product}")