#faça um programa que simule um caixa eletrônico

print('-' * 35)
print('-          Banco Fodastico        -')
print('-' * 35)

valor = int(input('Digite o valor que deseja sacar R$'))
total = valor
cédulas = 50
total_ced = 0

while True:
    if total >= cédulas:
        total -= cédulas
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${cédulas}.')
        if cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 1
        total_ced = 0
        if total == 0:
            break
print('=' * 35)
print('Volte sempre ao Banco Fodastico.')
