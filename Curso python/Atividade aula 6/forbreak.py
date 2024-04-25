## comando for com break. 


from  random import randint
aleatorio = randint(0,20)


# inicio fim salto     i  f s
for elemento in range (1,11,1) : 
 
    n1= int(input(f"Rodada -{elemento}   Digite um numero : "))
    if n1 == aleatorio:
        print("Voce ganhou :DD")
        break

    