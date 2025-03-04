#faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    print('-=' * 30)
    print('Analisando os valores...')
    print(f'Dentre os números: ', *num)
    sleep(0.6)
    print(f'O maior deles é: {max(num)}\n')
    sleep(0.6)


maior(1, 3, 9, 4, 5)
maior(100, 23, 2, 4, 101)
maior(500, 12, 3)
