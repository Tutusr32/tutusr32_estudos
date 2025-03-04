#faça um programa que leia os catetos e descubra o valor da hipotenusa

import math

cateto_adj = float(input('Digite o cateto adjacente:'))
cateto_opst = float(input('Digite o cateto oposto:'))

print(f'A hipotenusa será de {math.sqrt(cateto_adj**2 + cateto_opst**2):.2f}')

