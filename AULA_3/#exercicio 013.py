#faça um programa que peça o salario de um funcionario e o aumento dele

salario = float(input('Qual é o salário do funcionário?: R$'))
aumento = float(input('Qual foi o aumento dele? (em %): '))

print(f'O funcionário com o salário de R${salario}, com {aumento}% de aumento, passará a receber {salario + (salario*aumento) / 100}')


