## DESAFIO 05

## Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
## de mostrar que tipo de triângulo será formado:
## Equilátero: Todos os lados iguais
## Isósceles: Dois lados iguais
## Escaleno: Todos os lados diferentes

#Equilátero: Todos os lados iguais

# Isósceles: Dois lados iguais

# Escaleno: Todos os lados diferentes



reta1 = int(input("Digite um numero "))   # Reta : A
reta2 = int(input("Digite um numero "))   # Reta : B
reta3 = int(input("Digite um numero "))   # Reta : C

ab = reta1 + reta2
ac = reta1 + reta3
bc = reta2 + reta3

if (ab>reta3) and (ac>reta2) and (bc>reta1) : 
    print( "é um triangulo ")
else:
    print( "nâo é um triangulo ")   
    
    
if ab == bc and bc == ac :
    print("O triangulo é Equilátero ! ")
    
elif  ab == bc or bc == ac:
    print("É um triangulo Isósceles ")
    
else :
    print("É um triangulo escaleno")
