#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    Para f: armazena o valor do fatorial
    para c: variável que participa do laço for
    para show: se show for False, o programa deverá mostrar apenas o resultado do fatorial, caso for True, deverá mostrar a conta inteira. Ex: 3 x 2 x 1 = 6
    """

    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

help(fatorial)
num = int(input('Digite o número: '))
print(fatorial(num))
print(fatorial(num, True))
