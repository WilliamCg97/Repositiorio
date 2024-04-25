

from datetime import *

#Data atual 
da= date.today()

#Ano atual 
aa = da.year

#mes atual 
## ma= da.month

#dia atual
## am= da.day 

mirim = 9
infantil = 14 
junior = 19 
senior = 24 
 
nascimento= int(input("Digite a data de seu nascimento "))


id = aa - nascimento 

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

