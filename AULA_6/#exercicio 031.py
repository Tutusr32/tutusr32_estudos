#faça um programa que diga o preço de uma passagem, e ao passar dos 200km ela fique mais barata por km

passagem = float(input('Quantos Km você vai viajar?:'))

if passagem <= 200:
    print(f'O preço da passagem para {passagem}Km, será de {passagem * 0.50} reais!')

else:
    passagem >=201
    print(f'O preço da passagem para {passagem}Km, será de {passagem * 0.45} reais!')
