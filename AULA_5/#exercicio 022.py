#faça um programa que peça o nome completo do usuario e deixe em aumentativo, diminutivo
# e fale quantas letras tem o nome inteiro (não inclui espaços) e conte quantas letras tem o prim nome

nome = str(input('Qual é o seu nome?:'))

print(f'Seu nome no aumentativo é {nome.upper()}')

print(f'Seu nome no diminutivo é {nome.lower()}')

print(f'Seu nome tem um total de {len(nome) - nome.count(' ')} letras!!')

print(f'Seu primeiro nome tem {nome.find(' ')} letras!!')
