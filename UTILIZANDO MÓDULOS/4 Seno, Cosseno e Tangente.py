#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do:
# seno, cosseno e tangente desse ângulo.

import math
angulo= float(input('Digite o Ângulo que deseja: '))

sen= math.sin(math.radians(angulo))
cos= math.cos(math.radians(angulo))
tang= math.tan(math.radians(angulo))

print ("O Seno do angulo de {} é {:.2f}".format(angulo,sen))
print ("O Cosseno do angulo de {} é {:.2f}".format(angulo,cos))
print ("A Tangente do angulo de {} é {:.2f}".format(angulo,tang))



