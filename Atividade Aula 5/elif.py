#aprovado >=50 
#Recuperação <50 and >=40 
# Reprovado <40 


n1 = int(input("Digite nota da sua primeira prova :  "))
n2 = int(input("Digite nota da sua segunda prova :  "))
n3 = int(input("Digite nota da sua terceira  prova :  "))


media=  (n1 + n2 + n3 / 3 )


if media >= 50 :
    print("Aluno Aprovrado !!! ")
    
elif media <= 40 and media <= 49 :
    print("Aluno de Recuperação :o  !! ")

else :  
    print("Aluno Repovado :/// ")
    
    
    
    