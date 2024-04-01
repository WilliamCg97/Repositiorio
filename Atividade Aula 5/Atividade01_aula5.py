## DESAFIO 01
## Escreva um programa para aprovar um empréstimo bancário
## para a compra de uma casa. O programa vai perguntar o valor
## da casa, o salário do comprador e em quantos anos ele vai
## pagar.

## Calcule o valor da prestação mensal, sabendo que ela não pode
## exceder 30% do salário ou então o empréstimo será negado.

## Salario 

n1 = float(input("Digite o seu salario : R$ "))

## Valor Casa 

vc =  float(input("Qual o valor da casa ? R$ "))

#tempo para pagar

t =  float(input("Quantos anos para pagar esse emprestimo ? "))

t1= t * 12 

# media parcela  

p =  vc / t1   

print(f"Valor da parcela {p}")

#Media exigida pelo banco.

me = 0.3 * n1 


print(f"Valor mensal 30% {me}")


if me >= p :
    print("Emprestimo aceito :DD ")
else :
    print(" Emprestimo negado ")


