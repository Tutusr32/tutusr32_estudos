#faça um programa que calcule um alistamento militar
from datetime import date

atual = date.today().year
ano = int(input('Digite seu ano de nascimento:'))
idade = atual - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')

if idade == 18:
    print(f'Você deve se alistar agora em {atual}')
elif idade >=19:
    print(f'Você deveria ter se alistado {idade - 18} ano(s) atrás, em {ano +18}!')
else:
    print(f'Você ainda não deve se alistar, faltam {18 - idade} ano(s) para o alistamento, e ocorrerá em {ano + 18}!')

