#Crie um programa que leia o nome e o preço de vários produtos. 
#o programa deverá perguntar se o usuário quer continuar e no final mostre:
#       A) Qual o total gasto na compra.
#       B) Quantos produtos custam mais de R$1000.
#       C) Qual o nome do produto mais barato

total = mais_1000 = menor_preco = contador = 0
nome_barato = ''

print('-' * 35)
print('     LOJA MUITO LEGAL     ')
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Preço do produto R$'))
    contador += 1
    total += preco

    if preco > 1000:
        mais_1000 += 1

    if  contador == 1 or preco < menor_preco:
        menor_preco = preco
        nome_barato = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_barato = produto
    
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Total da compra: {total}')
print(f'Quantos produtos custam mais de R$1000: {mais_1000}.')
print(f'O produto {nome_barato} é o produto mais barato, custando: {menor_preco}')

