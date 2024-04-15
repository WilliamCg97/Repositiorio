
operador= None 

while True : 
    
    
    n1 = float(input ("Digite o primeiro valor : " ))

    n2 = float(input("Digite o segundo valor :"))

    print("Operadores : + , - , * , / . ")
    operador = input (" Digite o operado : ")
    

    if operador == "+" : 
        resultado = n1 + n2 
        print(resultado) 

    elif operador == "-" :
        resultado = n1 - n2 
        print (resultado)

    elif operador == "*" : 
        resultado = n1 * n2 
        print (resultado) 

    elif operador == "/" : 
        resultado = n1 / n2 
        print (resultado)

    print("Digite qualquer letra  para parar de calcular ")
    stop = input("Deseja encerrar ? digite s/n ").upper

    if stop != "N" :
        break



