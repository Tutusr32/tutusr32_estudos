#faça um programa em que após um carro ultrapassar do km/h 80, dê 7 reais de multa por km.

import math

carro = int(input('Em quantos km/h.s estava seu carro?:'))
kmh = carro


if carro > 80:
    print(f'Com {carro}km/h, você pagará R${kmh *7}!')

else:
    carro <= 79
    print('Isento de multa!')

    