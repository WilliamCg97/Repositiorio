#tranformando a string 

frase = "Microsoft Power BI"

#trocando uma palavra 

troca= frase.replace("Power BI" , ":D :D :D ")
print(troca) 

#Converter todas as letras para maiusculas. 

print(frase.upper())

#Converter todas as letras para minusculas. 

print(frase.lower())

#modifcando a primeira letra para  maiusculo  

print(frase.capitalize())

#converte a primeira letra de cada palvra da frase;

print(frase.title())

#Retirando os espaços no inicio e no fim do texto. 

curso= "                  Fundamentos da cienciade dados - google                         " 
print(curso.strip())

print(curso.rstrip())    # Remove os espaçoes da direita " right"
print(curso.lstrip())    # Remove os espaços da esquerda " left "