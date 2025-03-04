#faça um programa que jogue Jokenpô com o usuário.

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual a sua jogada?: '))
print(f'O computador escolheu {itens[computador]}')

if jogador == computador:
    print('EMPATE!')
elif jogador == 0 and computador == 2:
    print('Jogador Venceu')
elif jogador == 1 and computador == 0:
    print('Jogador Venceu')
elif jogador == 2 and computador == 1:
    print('Jogador Venceu')
elif computador == 2 and jogador == 1:
    print('Computador Venceu')
elif computador == 1 and jogador == 0:
    print('Computador Venceu')
elif computador == 0 and jogador == 2:
    print('Computador Venceu')
else: 
    print('Escolha um número entre 0 até 2!')
    