## DESAFIO 03
## Crie um programa que leia duas notas entre 0 a 10 de um aluno
## e calcule sua média, mostrando uma mensagem no final, de
## acordo com a média atingida.
## 
## Média abaixo de 5.0: REPROVADO
## Média entre 5.0 a 6.9: RECUPERAÇÃO
## Média igual ou superior a 7.0: APROVADO

m = 7
mf = 5
md = 6.9


n1 =float(input("Digite sua primeira nota : ")) 
n2 =float(input("Digite sua segunda nota : "))

media = (n1 + n2) / 2

if n1 <= 10 and n1 >=0 and n2 <= 10 and n2 >=0 :
      

    if media <= mf :
        print("Reprovado")
        print(f"A media das suas notas é : {media}")
    elif media <= md and media >= mf :
        print("Recuperação") 
        print(f"A media das suas notas é : {media}")
    else:
        print("Aprovado :D ")
        print(f"A media das suas notas é : {media}")
else :
    
    print("Favor informar a notas de 0 a 10 .")