#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

from time import sleep


def ajuda(com):
    print(f'Acessando manual do comando {com}..')
    sleep(1.5)
    help(com)
    print()

while True:
    print('Sistema de ajuda PyHelp.')
    com = str(input('Função ou Biblioteca > '))
    if com.upper() == 'FIM':
        break
    else:
        ajuda(com)
print('Até mais..')
