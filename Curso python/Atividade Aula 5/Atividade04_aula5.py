## DESAFIO 04
#
## A confederação Nacional de Natação precisa de uma programa
## que leia o ano de nascimento de uma atleta e mostre sua
## categoria, de acordo com a idade.

## Até 9 anos: MIRIM
## Até 14 anos: INFANTIL
## Até 19 anos: JUNIOR
## Até 24 anos: SÊNIOR
##  Acima: MASTER


n1 = int(input("Favor digitar ano de nascimento: ---- "))

# Parametros
mirim = 9
infantil = 14 
junior = 19 
senior = 24 
 
# Idade
id = 2024 -n1  


if id <= mirim :
    print("Classificado como Mirim !! ")

elif id > mirim and id <= infantil :
    print("Voce foi classificado como Infantil ! ") 
    
elif id > junior and id < senior :
    print("Você foi classificado como junior !! ")

elif id < senior :
    print("Você se enquandra na classificão Senior !! ")
    
else :
    print("Você foi classificado como categoria Master !!! ")



## "from datetime import* " forma de pegar a data atual sem colocando direto o numero "2024 "
## Comando "From" para importar "Datetime " seria a biblioteca, "import *" seria importar tudo da biblioteca 







