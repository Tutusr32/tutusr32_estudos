#faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    print(f'Largura de {largura} x comprimento de {comprimento} = {a}m^2.')

largura = float(input('Qual o valor da largura: '))
comprimento = float(input('Qual o valor do comprimento: '))

area(largura, comprimento)

