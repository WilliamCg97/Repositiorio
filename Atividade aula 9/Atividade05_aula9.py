## Crie um programa que tenha uma tupla única com nomes de produtos
## e seus respectivos preços, na sequência.

## No final, mostre uma listagem de preços, organizando os dados em
## forma tabular.





l1 = [ 'R$ 5' , 'R$ 5' , 'R$ 5' , 'R$ 15' , 'R$ 15' , 'R$ 16' ]
l2= ['coca' , 'pastel ' , 'coxinha ' , 'frango ' , 'pf ' ,'pf 2' ]


l3 = l1 + l2 

for loop in range (0 , 1 ,1 ) : 
    
    
    tupla = tuple(zip(l2, l1))
    print(tupla)
  

