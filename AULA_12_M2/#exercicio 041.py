#faça um programa que classifique atletas nadadores
from datetime import date

atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano

print(f'O atleta tem {idade} anos de idade!')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade >= 9 and idade <=14:
    print('Classificação: INFANTIL')
elif idade >= 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade >= 19 and idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
    