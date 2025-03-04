# faça um programa que leia o nome, a idade e o sexo de 4 pessoas. E no final mostre essas informações:
#         A média de idade do grupo -- Qual o homem mais velho -- Quantas mulheres tem acima de 20 anos.

m = 0
velho = ''
m_idade = 0
totmulher20 = 0

for c in range(1, 5):
    print(f'----- {c}º PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    m_idade += (idade) / 4
    
    if c == 1 and sexo in 'Mm':
        m = idade
        velho = nome
    
    if sexo in 'Mm' and idade > m:
            m = idade
            velho = nome
    if sexo in 'Ff' and idade < 20:
         totmulher20 = totmulher20 +1

print(f'A média de idade do grupo é de {m_idade} anos.')

print(f'O homem mais velho tem {idade} e se chama {velho}.')

print(f'Existem {totmulher20} mulheres abaixo dos 20 anos no grupo.')


