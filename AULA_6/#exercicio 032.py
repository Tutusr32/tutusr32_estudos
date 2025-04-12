#faça um programa que receba um ano, e diga se ele é bissexto ou não

from datetime import date

ano = int(input('Digite um ano (digite 0 para saber sobre o ano atual):'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano}, é BISSEXTO')
else:
    print(f'O ano de {ano}, NÃO é bissexto')
