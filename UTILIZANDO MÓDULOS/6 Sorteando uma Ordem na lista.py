#Sortear a ordem de apresentação de trabalhos dos 4 alunos


from random import shuffle

Aluno1= str(input ("Primeiro Aluno:"))
Aluno2= str(input ("Segundo Aluno:"))
Aluno3= str(input ("Terceiro Aluno:"))
Aluno4= str(input ("Quarto Aluno:"))

Lista= [Aluno1, Aluno2, Aluno3, Aluno4]

# Shuffle significa EMBARALHAR 
shuffle(Lista)


print ("A ordem de Apresentações será:\n{}".format(Lista) )