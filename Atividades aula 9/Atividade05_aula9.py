## Crie um programa que tenha uma tupla única com nomes de produtos
## e seus respectivos preços, na sequência.

## No final, mostre uma listagem de preços, organizando os dados em
## forma tabular.





l1 = [ 5 , 5 , 5 , 15 , 15 , 16 ]
l2= ['coca' , 'pastel ' , 'coxinha ' , 'frango ' , 'pf ' ,'pf 2' ]


l3 = l1 + l2 

for loop in range (0 , 6 ,1 ) : 
    print (l2[loop] , '- R$' , l1 [loop] )
    
    f= tuple(loop)
    print(f)
  

