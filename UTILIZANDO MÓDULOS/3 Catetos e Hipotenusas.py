#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

#OPÇÃO 1 DE RESOLVER:

oposto= float  (input ('Comprimento do Cateto Oposto:') )
adjacente= float ( input ('Comprimento do Cateto Adjacente:'))

hipotenusa= (oposto**2 + adjacente**2) ** (1/2)

print ("A Hipotenusa vai medir {:.2f}".format(hipotenusa) )


#OPÇÃO 2 DE RESOLVER (Importando Biblioteca de Matemática):

import math

oposto= float  (input ('Comprimento do Cateto Oposto:') )
adjacente= float ( input ('Comprimento do Cateto Adjacente:'))

hipotenusa= math.hypot(oposto,adjacente)

print ("A Hipotenusa vai medir {:.2f}".format(hipotenusa) )


