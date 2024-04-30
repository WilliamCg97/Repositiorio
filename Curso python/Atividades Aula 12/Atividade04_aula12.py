# DESAFIO 01

# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.
while True : 
    try  : 
    
        n1 = int (input("Digite o primeiro valor "))
        n2 = int (input("Digite o segundo valor "))
        div = n1 / n2 
    
    except ZeroDivisionError : 
        print ('nao existe divisao de inteiro por 0  ! ')
 
    except ValueError : 
        print ("Digite somente numeros ")
   
    else : 
        print (f"O valor da divisão foi {div}")
        break