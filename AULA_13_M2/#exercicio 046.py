#faça um programa que faça uma contagem regressiva de 10 até 0 com um emoji de fogos de artifício no fim.

import time
import emoji

soma = 0
for cu in range(10, -1, -1):
    print(cu)
    time.sleep(1)
print(emoji.emojize('Feliz Ano Novo!! :fogos_de_artifício:', language='pt'))
