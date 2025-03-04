#faça um programa que replique o jogo do ímpar ou par

from random import randint
computador_pi = ''
computador = randint(0, 10)
print('-' * 30)
print('***** JOGO DO ÍMPAR OU PAR *****')
contador_vitoria = 0

while True:
    jogador = int(input('Digite um número de 1 até 10: '))
    impar_par = str(input('Ímpar ou Par? [I/P]: ')).strip().upper()[0]
    soma = jogador + computador

    if impar_par in 'Ii':
        computador_pi == 'Par'
        print(f'O jogador jogou {jogador} e o computador escolheu {computador}, total de {soma}!')
        print('O computador escolheu PAR!!')
    elif impar_par in 'Pp':
        computador_pi == 'Ímpar'
        print(f'O jogador jogou {jogador} e o computador escolheu {computador}, total de {soma}!')
        print('O computador escolheu ÍMPAR!!')
    else:
        print('Digite um valor válido!')
        break

    if soma % 2 == 0:
        print(f'PAR GANHOU!')
        if impar_par in 'Pp':
            print('Jogador Ganhou')
            contador_vitoria += 1

        elif computador_pi in 'Par':
            print('Computador Ganhou!')
            print(f'Você perdeu, com um total de {contador_vitoria} vitórias consecutivas!')
            novamente = str(input('Deseja continuar? [S/N]: '))
            if novamente in 'Nn':
                break
        else:
            break
    if soma % 2 != 0:
        print('ÍMPAR GANHOU!')
        if impar_par in 'Ii':
            print('Jogador Ganhou')
            contador_vitoria += 1

        elif computador_pi in 'Ímpar':
            print('Computador Ganhou!')
            print(f'Você perdeu, com um total de {contador_vitoria} vitórias consecutivas!')
            novamente = str(input('Deseja continuar? [S/N]: '))
            if novamente in 'Nn':
                break

        else:
            break
print('Programa encerrado...')


            