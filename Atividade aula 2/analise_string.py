t1= "Curso de python"
name = "William Costa"
##Analisar o tamnho da frase. 

print(len(t1))
print(len(name))

## Conta quantas vezes um caracter especifico aparece.

print(t1.count("o")) 
print(name.count("o"))

#Indica a posição de inicio de uma frase desejada.

print(t1.find("python"))
print(name.find("Costa"))

#verificando se possui a palavra em uma frase.

print("python"in t1 )
print("Silva"in name )
print("Siqueira"in name )
print("Santos"in name )
print("Souza"in name )
print("Ribeiro"in name )

