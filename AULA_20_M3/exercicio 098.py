#faça um programa que tenha uma função chamada contador(), que recebe três parâmetros: Início, fim e passo e realize a contagem.
#Seu programa tem que realizar três contagens através da função criada:
#A) De 1 até 10, de 1 em 1.
#B) De 10 até 0, de 2 em 2.
#C) Uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passos):
    for c in range(1, 11):
        print(f'{c}', end= ' ', flush=True)
        sleep(0.5)
    print()

    for b in range(10, -2, -2):
        print(f'{b}', end= ' ', flush=True)
        sleep(0.5)

    print()
    print('Agora é a sua vez, faça a sua contagem personalizada.')
    print()

    inicio = int(input('Diga o ínicio: '))
    fim = int(input('Diga o fim: '))
    passos = int(input('Os passos: '))

    if passos != 0:
        if inicio > fim:
            for i in range(inicio, fim-passos, -passos):
                print(f'{i}', end= ' ', flush=True)
                sleep(0.5)
        else:
            for i in range(inicio, fim+1, passos):
                print(f'{i}', end= ' ', flush=True)
                sleep(0.5)
    print()


contador(1, 11, 1)