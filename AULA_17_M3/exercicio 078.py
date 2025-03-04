#faça um programa que leia 5 valores numéricos e guarde-os em uma lista
#no final mostre o maior e o menor número da lista e suas respectivas posições

num = []

for numeros in range(0, 5):
   num.append(int(input('Digite os valores: ')))

print(f'Os números da lista são: {num}')

print(f'O maior número da lista é {max(num)} na posição', end=' ')
for posição, valores in enumerate(num):
    if valores == max(num):
        print(f'{posição + 1}...', end='')

print()

print(f'O menor número da lista é {min(num)} na posição', end=' ')
for posição, valores in enumerate(num):
    if valores == min(num):
        print(f'{posição + 1}...', end='')
