## DESAFIO 03

## Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
## do Campeonato Brasileiro Serie B de Futebol, na ordem de
## colocação. Depois mostre:

## A) Apenas os 5 primeiros colocados.

## B) Os últimos 4 colocados da tabela.

## C) Uma lista com os times em ordem alfabética.

## D) Em que posição na tabela está o time do Santos.   



lista_times= ('palmeiras SP' ,  'gremio' ,  'atletico Mineiro MG' ,  'flamengo' ,  'botafogo FR RJ',  'red Bull Bragantino SP' ,  'fluminense RJ' ,  'ca Paranaense PR' ,  'internacional RS' , 'fortaleza CE' , 'são Paulo' , 'cuiabá Esporte Clube MT' , 'corinthians SP' , 'cruzeiro' , 'vasco Gama' , 'bahia' , 'santos FC SP' , 'goiás EC GO' , 'coritiba PR' , 'américa FC MG')

## mostrando apenas da atividade a e b . 

print(lista_times[0:5])
print(lista_times[-4 : ])

## c 
lista_ordenada = sorted(lista_times)
print (lista_ordenada)

print (lista_times[16])



