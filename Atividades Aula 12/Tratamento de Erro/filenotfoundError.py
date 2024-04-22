# ele ocorre quando tenta selecionar um arquivo porem o endereço esta errado ou o arquivo nao existe .


try : 
    with open("data.txt" , "r") as arquivo : 
        conteudo = arquivo.read ()
        
except FileNotFoundError :
    print ("este arquivo nao existe  ")
    