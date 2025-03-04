#crie um programa que vai gerar 5 números aleatórios em uma tupla. Depois disso mostre a listagem de números e indique o menor e o maior valor gerado.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)

print('Foram sorteados os valores:', end= ' ')
for num in numeros:
    print(f'{num}', end= ' ')

print(f'\nO maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')
