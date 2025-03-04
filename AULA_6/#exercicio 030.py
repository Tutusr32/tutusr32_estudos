#faça um programa que diga se um número é ímpar ou par.

n1 = int(input('Digite um número!:'))

par = n1 % 2


if par == 0:
    print('PAR!')
else:
    print('IMPAR!')

