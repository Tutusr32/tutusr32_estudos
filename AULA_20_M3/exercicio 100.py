#faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista. A segunda função vai mostrar a soma entre os valores Pares sorteados pela função anterior.

num = []

from random import randint

def sorteia():
    for c in range(1, 6):
        num.append(randint(1, 10))
    print(f'Os números sorteados foram: {num}')

sorteia()

def somapar():
    soma = 0
    for par in num:
        if par % 2 == 0:
            soma += par
    print(f'A soma dos números pares é: {soma}')

somapar()
