#faça uma calculadora com multi-opções de calculos e números

import time

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0

while opção != 5:
    print('''
[ 1 ] Somar.
[ 2 ] Multiplicar.
[ 3 ] Maior número.
[ 4 ] Novos números.
[ 5 ] Sair do Programa.          
''')
    opção = int(input('Digite a sua opçã0: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é de {soma}!')
    elif opção == 2:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é de {multi}!!')
    elif opção == 3:
        if n1 > n2:
            print(f'O número {n1} é o maior!')
        elif n2 > n1:
            print(f'O número {n2} é o maior!')
        elif n1 == n2:
            print('Os números são iguais!')
    elif opção == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opção == 5:
        print('Encerrando programa...')
        time.sleep(2)
    else:

        print('Opção inválida, tente uma opção dentre as opções abaixo:')
print('Fim do programa.')
