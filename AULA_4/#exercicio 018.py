#faça um programa que meça Seno, Cosseno e Tangente

import math

ang = float(input('Digite o ângulo:'))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print(f'O ângulo de {ang}, tem o seno de {seno:.2f}, o cosseno de {cosseno:.2f} e o tangente de {tangente:.2f}!!')

