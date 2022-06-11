# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na Tela:
# Nome do escolhido.

import random

Aluno1= str(input ("Primeiro Aluno:"))
Aluno2= str(input ("Segundo Aluno:"))
Aluno3= str(input ("Terceiro Aluno:"))
Aluno4= str(input ("Quarto Aluno:"))

#Crie uma lista, exemplo: Compras = [ banana, maça, uva ]

Lista= [Aluno1, Aluno2, Aluno3, Aluno4]

#random.choice é uma escolha aleatória 
Sorteado= random.choice( Lista )


print ("O ALUNO SORTEADO FOI {}".format(Sorteado) )
