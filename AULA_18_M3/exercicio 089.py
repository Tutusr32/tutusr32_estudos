#crie um programa que leia nome e duas notas de vários alunos e gaurde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as nnotas de cada aluno individualmente
from time import sleep

ficha = []
contador = 0
aluno_nota = 0

while True:
    nome = str(input('Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    contador += 1

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if continuar in 'n':
        break
    else:
        if continuar in 's':
            continue
        else:
            print('Você precisa escolher entre S ou N!!')

print('-' * 30)
print(f'{'No. Nome':<10} {'Média':>13}')
print('-' * 30)

for c in range(0, contador):
    print(f'{0 + c} {ficha[0 + c][0]:>4}', end='')
    print(f'{ficha[0 + c][2]:>22.2f}')
print('-' * 30)

while True:
    aluno_nota = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))

    if aluno_nota <= len(ficha) - 1:
        print(f'As notas do Aluno: {ficha[aluno_nota][0]}. São: {ficha[aluno_nota][1]}')

    if aluno_nota == 999:
        print('Finalizado...')
        sleep(2)
        break

print(f'{'-=' * 10} {'Volte Sempre!':^10} {'-=' * 10}')
