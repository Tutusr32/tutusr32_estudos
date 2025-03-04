#faça um programa que escolha aleatoriamente entre uma lista de alunos

import random

alun1 = str(input('Digite o nome do aluno:'))
alun2 = str(input('Digite o nome do aluno 2:'))
alun3 = str(input('Digite o nome do aluno 3:'))
alun4 = str(input('Digite o nome do aluno 4:'))

lista = (alun1, alun2, alun3, alun4)

print(f'O aluno escolhido foi {random.choice(lista)}')

