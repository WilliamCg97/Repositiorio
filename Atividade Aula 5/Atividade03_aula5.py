## DESAFIO 03
## Crie um programa que leia duas notas entre 0 a 10 de um aluno
## e calcule sua média, mostrando uma mensagem no final, de
## acordo com a média atingida.
## 
## Média abaixo de 5.0: REPROVADO
## Média entre 5.0 a 6.9: RECUPERAÇÃO
## Média igual ou superior a 7.0: APROVADO



n1 =float(input("Digite sua primeira nota : ")) 
n2 =float(input("Digite sua segunda nota : "))
n3 =float(input("Digite sua terceira  nota :"))


m = 7
mf = 5
md = 6.9

media = (n1 + n2 + n3 ) / 3 

print(f"A media das suas notas é : {media}")

if media <= mf :
    print("Reprovado")
    
elif media <= md and media >= mf :
    print("Recuperação") 

else:
    print("Aprovado :D ")
