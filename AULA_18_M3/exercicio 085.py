#crie um programa onde o usuário possa digitar sete valores númericos e os cadastre em uma lista única que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e ímpares de forma crescente

num = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))

    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 == 1:
        num[1].append(valor)

num[0].sort()
num[1].sort()

print(f'Os valores pares foram {num[0]}. E os valores ímpares foram {num[1]}')
