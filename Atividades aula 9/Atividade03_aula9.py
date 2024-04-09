## DESAFIO 03

## Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
## do Campeonato Brasileiro Serie B de Futebol, na ordem de
## colocação. Depois mostre:

## A) Apenas os 5 primeiros colocados.

## B) Os últimos 4 colocados da tabela.

## C) Uma lista com os times em ordem alfabética.

## D) Em que posição na tabela está o time do Santos.   



lista_times= (' Palmeiras SP' ,  'Gremio' ,  'Atletico Mineiro MG' ,  'Flamengo' ,  'Botafogo FR RJ',  'Red Bull Bragantino SP' ,  'Fluminense RJ' ,  'CA Paranaense PR' ,  'Internacional RS' , 'Fortaleza CE' , 'São Paulo' , 'Cuiabá Esporte Clube MT' , 'Corinthians SP' , 'Cruzeiro' , 'Vasco Gama' , 'Bahia' , 'Santos FC SP' , 'Goiás EC GO' , 'Coritiba PR' , 'América FC MG')

## mostrando apenas da atividade a e b . 

# print(lista_times[0:5])
# print(lista_times[-4 : 20])

## c 
lista_ordenada = sorted(lista_times).upper()
print (lista_ordenada)




