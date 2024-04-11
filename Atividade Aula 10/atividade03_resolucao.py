lista = [] #10

for c in range(0,5):    
    n = int(input("Digite um valor: ")) #10 ,1, 15,20,7   c=2

    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):  # 2<2
            if n <= lista[pos]: # 15<10
                lista.insert(pos,n)# lista = [1,10,15,20]
                print(f"Adicionado na posição {pos} da lista")
                break
            pos += 1

print(f"Os valores digitados em ordem foram {lista}")