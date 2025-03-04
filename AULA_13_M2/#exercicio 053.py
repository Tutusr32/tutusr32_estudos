#faça um programa que detecte um palíndromo

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[c]

print(f'o inverso de {junto} é {inverso}!!')   
if inverso == junto:
    print('Temos um palídromo')
else:
    print('Não temos um palíndromo')

