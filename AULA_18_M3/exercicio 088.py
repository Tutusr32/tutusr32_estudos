#faça um programa que ajude um jogador da mega-sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep
contador = 0
lista = []
lista_jogos = []
jogos = int(input('Quantos jogos deseja sortear?: '))
cont_jogos = 1

while cont_jogos <= jogos:
    cont_jogos += 1

    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    lista_jogos.append(lista[:])
    lista.clear()
    contador = 0

print(f'Sorteando {jogos} Jogos da Mega-Sena!')
print('...')
sleep(1.5)
for c in range(0, jogos):
    print(f'Jogo {c + 1}: {lista_jogos[0 + c]}')
    print('...')
    sleep(2)
print('Fim!!')
