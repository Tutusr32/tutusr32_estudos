# faça um programa que leia o primeiro termo e a razão de uma progressão aritimética e mostre os 10 primeiros termos


primeiro = int(input('Digite o primeiro termo: '))

razão = int(input('Digite a razão: '))

decimo = primeiro + (10 - 1) * razão


for c in range(primeiro, decimo + razão, razão):
    print(f'{c} ', end='→ ')
print('Acabou.')
