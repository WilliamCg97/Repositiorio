#aprovado >=50 
#Recuperação <50 and >=40 
# Reprovado <40 


n1 = float(input("Digite nota da sua primeira prova entre 0 a 7: "))
n2 = float(input("Digite nota da sua primeira Atividade  entre 0 a 3 :" ))



#Notas da prova é igual a 70% da nota final 
#nota das atividades = 30% da media final 

media=  (n1 + n2 ) 
print(f"Media das notas  : {media}")

if media >= 5 :
    print("Aluno Aprovrado !!! ")
    
elif media >= 4 :
    print("Aluno de Recuperação :o  !! ")

else :  
    print("Aluno Repovado :/// ")
    
    
    
    