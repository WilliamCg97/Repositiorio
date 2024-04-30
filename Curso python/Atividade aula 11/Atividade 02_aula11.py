# DESAFIO 02

# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultado aleatórios. Guarde esses resultados em um
# dicionário . No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior numero no dado.


from random import randint
from time import sleep
from operator import itemgetter



j1 =randint( 0,6)
j2 =randint( 0,6 )
j3 =randint( 0,6 )
j4 =randint( 0,6 )

lista_de_jogadas=[]
lista_de_jogadas.append(j1)
lista_de_jogadas.append(j2)
lista_de_jogadas.append(j3)
lista_de_jogadas.append(j4)


m_jogada=max( lista_de_jogadas)
ordem =sorted(lista_de_jogadas)

dcn = [ 
 { "jogador 1" : [j1] , 
  "jogador 2" : [j2] , 
  "jogador 3" : [j3] , 
  "jogador 4" : [j4] , 
  "jogadas ordenas " : [ordem] ,
   "Maior jogada " : [m_jogada]  }  ]

print(dcn)


# dcn = {
    
    
    
    
    ## Resolução 
# meuDicionario = {
#     "jogador1" : randint(1,6),
#     "jogador2" : randint(1,6),
#     "jogador3" : randint(1,6),
#     "jogador4" : randint(1,6)
# }

# for k, v in meuDicionario.items():
#     print(f"{k} tirou {v} no dado")
#     sleep(1)

# # print(meuDicionario)

# print("Em ordem crescente")

# #sorted(iterable, key=key, reverse=reverse)
# #sorted(Quem?, qual a chave, Quer inveter?)
# ranking = sorted(meuDicionario.items(), key=itemgetter(1), reverse=True)
# print(ranking)

# for i, v in enumerate(ranking):
#     print(f"{i+1}° lugar: {v[0]} com {v[1]}")
#     sleep(1)