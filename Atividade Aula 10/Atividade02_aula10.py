    # DESAFIO 02

    # Crie um programa onde o usuário possa digitar vários valores
    # numéricos e cadastre-os em uma lista. Caso o número já
    # exista lá dentro, ele não será adicionado. No final serão
    # exibidos todos os valores únicos digitados, em ordem
    # crescente.

## comando in  para verificar se ele esta dentro da lista 
## not se ele nao se encontra dentro da lista
lista=[]


while True : 
    
    
    n2 = input("Deseja registra um numero na lista S/N ").upper()
 
    if n2 == "S":
        
        n1 = int(input("Digite o numero que deseja cadastrar "))
        if n1 not in lista : 
            
            lista.append(n1)
            print("numero registrado na lista ")      
          

        else :
         print ("numero ja cadastrado, Favores registrar outro numero ")
         print (lista)   
            
    elif n2 == "N" :  
        print(lista)
        break
    else :
        print("Digite somente os caracteres informados.")

    lista.sort()
    






#   lista.append(n1)