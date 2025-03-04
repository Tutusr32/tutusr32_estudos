#crie um programa que verifique um empréstimo, e negue valores acima de 30% do salário.

valor = float(input('Qual é o valor da casa?:'))
salario = float(input('Qual é o seu salário?:'))
anos = int(input('Quantos você vai pagar?:'))
meses = 12 * anos
prest_mensal = valor / meses
porcentagem = ((30*salario) / 100)

if prest_mensal <= porcentagem:
    print(f'Com um imóvel de R${valor}, você pagará {porcentagem} por mês.')
else:
    print('Negado')
