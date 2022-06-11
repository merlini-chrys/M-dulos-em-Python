
# Vamos importar a biblioteca de Matemática " math "
# Para chamar a funcão específica é " math. "
# Arredondar um número para cima é " math.ceil( ) " 
# Arredondar um número para baixo é " math.floor( ) " 

import math

numero = int ( input('Digite um Número: '))
raizquadrada= math.sqrt(numero)

print ( 'A raiz quadrada de {} é {}'.format (numero, math.floor(raizquadrada) )  )