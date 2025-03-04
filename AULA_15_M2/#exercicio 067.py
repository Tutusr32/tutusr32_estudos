#faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O progarama será interrompido quando o número digitado for negativo.

from time import sleep

while True:
    num = int((input('Digite um valor: ')))
    if num < 0:
        print('Número negativo detectado, programa encerrando..')
        sleep(2)
        break
    for c in range(0, 11):
        print(f'{num} X {c} = {num * c}')
print('Programa encerrado.')

