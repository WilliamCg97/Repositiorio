#Crie um programa que tenja uma tupla totalmente preenchida com uma contagem por extenso , de zero até vinte.
#Seu programa deverá ler um numero pelo teclado (Entre 0 e 20) e mostralo por extenso




 ## tupla do 0 ao vinte por extenso 
tupla = ('zero' , 'um' , 'dois ', ' três', 'quatro ', 'cinco ', ' seis', 'sete ', ' oito', 'nove ', 'dez ', ' onze', ' doze', ' treze ', ' quatorze ', ' quinze ', 'dezesseis ', ' dezessete', 'dezoito ', 'dezenova ', ' vinte ', ' ' )



## Repetição importando numero que o usuario deseja e deixando escrito por extenso 



while True : 
    n1 = int(input("Digite um numero de 0 a 20 :  "))
    print (tupla[n1])
    
    n2 = input("Deseja continuar s/n :").upper()
    
    if n2 != 'S' :
        break




