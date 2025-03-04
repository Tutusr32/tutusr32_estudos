#faça um programa que compare números, dizendo o maior ou se são iguais

valor_1 = float(input('Digite um valor:'))
valor_2 = float(input('Digite outro valor:'))

if valor_1 > valor_2:
    print(f'O valor {valor_1} é maior que {valor_2}!')
elif valor_2 > valor_1:
    print(f'O valor {valor_2} é maior que {valor_1}!')
else:
    print('Os valores são iguais!')
