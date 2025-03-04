#faça um programa que dê um aumento de 15% para salarios abaixo de 1250, se for maior, de um aumento de 10%

salario = float(input('Qual é o valor do seu salário?:'))

if salario <= 1249:
    print(f'Com um salário de R${salario}, você passará a receber R${salario + (salario*15)/ 100}')
else:
    salario >= 1250
    print(f'Com um salário de R${salario}, você passará a receber R${salario + (salario*10)/100}')

