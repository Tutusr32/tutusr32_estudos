#aprimore o desafio anterior e mostre no final:
#A) A soma dos valores pares
#B) A soma dos valores da 3o. coluna
#C) O maior valor da 2o. linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = s_col = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha, coluna}: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end= '')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()

print(f'A soma dos números pares é {pares}')
for linha in range(0, 3):
    s_col += matriz[linha][2]
print(f'A soma dos elementos da 3o. coluna é {s_col}')
print(f'O maior valor da 2o. linha é {max(matriz[1])}')

    