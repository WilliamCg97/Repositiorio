# DESAFIO 01

# Faça um programa que leia o nome e média de um aluno,
# guardando também a situação em um dicionário. No final
# mostre o conteúdo da estrutura na tela.


# n1= None
# valores= []
# media= []
# ar = None


# dcn = [
# {"nome :" : [n1] ,
#   "media" : [media],
#   "resultado" : [ar] 

#  }    ]


# while True : 
    
#     n1 = input("Digite nome para cadastro ; ") 
#     dcn.append(n1[0])
    
    
#     for i in range (0,2) :
#         n2 = int(input("Digite as duas notas : "))
#         valores.append(n2)
    
#         if i == 2 : 
#             soma = valores [0] + valores [1]
#             media = soma / i
#             dcn [1]= media 
            
#         elif media >= 7 :
#             ar = "Aprovado"
#             dcn.append(ar)
#         else :
#             ar= "Reprovado"
#             dcn.append(ar)
        
            
#     print (valores)
    
    
    
#     print (f"{dcn}")
      
media= None
 

n1= input("Digite seu nome : ")
n2 =int(input("Digite sua media "))

if n2 >= 7 : 
    ar = "Aprovado"
else : 
    ar = "Reprovado"

dcn = [
    {
     "Nome : " : [n1] ,
     "media : " :  [n2],
     "A/R" : [ar]       }   
     ]

print (dcn) 