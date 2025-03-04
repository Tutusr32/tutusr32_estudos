#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o ganhador tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter


dado = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('Sorteando os valores...')
sleep(1.5)

for keys, values in dado.items():
    print(f'{keys} tirou {values} no dado.')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse='True')

print(f'{'-=-=-=-=-=-=-=RANKING=-=-=-=-=-=-=-':^15}')

for i, v in enumerate(ranking):
    print(f'{i + 1}o. lugar: {v[0]} com {v[1]} no dado.')
    sleep(1)
