#faça um programa que leia o sexo de uma pessoa, caso for digitado o valor errado, repita até um valor válido foi escrito

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor digite novamente: ')).upper().strip()[0]

print(f'Sexo {sexo} registrado com sucesso!')
