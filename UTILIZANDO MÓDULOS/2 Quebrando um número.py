#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#Ex: Digite um número: 6.127
#O número 6.127 tem a parte Inteira 6.


#OPÇÃO 1 DE RESOLVER 


# de math importar trunc ( "da biblioteca math importar somente a função trunc")
from math import trunc


n= float (input ("Digite um valor: "))



print ("O valor digitado foi {} e a sua porção inteira é {}" .format(n,trunc(n) ) )

#usamos math.trunc()
# que significa cortar, e deixar somente número inteiro  


#OPÇÃO 2 DE RESOLVER 


n= float (input ("Digite um valor: "))



print ("O valor digitado foi {} e a sua porção inteira é {}" .format(n,int(n) ) )