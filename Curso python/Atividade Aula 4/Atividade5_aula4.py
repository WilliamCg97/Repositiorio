## Desenvolva um programa que leia o comprimento de três retas
## e diga ao usuário se elas podem ou não formar um triângulo.
## Condições Necessárias:

# a + b > c

# a + c > b

# b + c > a


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
    
    