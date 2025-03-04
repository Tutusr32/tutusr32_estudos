#faça um programa que diga o maior resultado e o menor de uma sequência

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa: '))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}KG.')
print(f'O menor peso foi de {menor}KG.')

