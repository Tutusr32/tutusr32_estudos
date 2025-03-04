#faça um programa que escolha um número de 0 à 5, e tente fazer o usuario acerta-lo

import random

num = int(input('Pensei em um número de 0 à 5, tente adivinhá-lo: '))

numero = random.randint(0, 5)

if num == numero:
    print('Parabéns, você me venceu!')

else:
    print(f'Eu ganhei, eu estava pensando no numero {numero} e não no {num}!')