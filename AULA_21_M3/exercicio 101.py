#Crie um programa que tenha uma função chamada voto(), que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.

from datetime import datetime

def voto(ano_nasci):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nasci

    if idade >= 18 and idade < 65:
        return f'{idade} anos, o voto é obrigatório.'
    if idade < 16:
        return f'{idade} anos, não vota.'
    if idade >= 16 < 18 or idade > 65:
        return f'{idade} anos, o voto é opcional.'

ano_nasci = int(input('Ano de nascimento: '))
print(voto(ano_nasci))
