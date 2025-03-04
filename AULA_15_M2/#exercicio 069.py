# Crie um programa que leia o nome e a idade de várias pessoa. A cada pessoa cadastrada,
# O pragrama deverá perguntar se o usuário quer ou não continuar. No final mostre:
#       A) Quantas pessoas tem mais de 18 anos.
#       B) Quantos homens foram cadastrados.
#       C) Quantas mulheres tem menos de 20 anos.

contador = mulher_menos20 = homens = mais_18 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais_18 += 1
    
    if sexo in 'Mm':
        homens += 1
    
    if sexo in 'Ff':
        if idade < 20:
            mulher_menos20 += 1
            
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print(f'temos {homens} homens no grupo, {mais_18} pessoa maiores de 18 anos e {mulher_menos20} mulheres menores de 20 anos.')