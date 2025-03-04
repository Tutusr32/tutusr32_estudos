# faça um programa que diga se ele é um número primo

num = int(input('Digite um valor: '))
total = 0

for c in range(1, num+1):
    if num % c == 0:
        print(f'{c}*', end=' ')
        total = total + 1
    else:
        print(f'{c}', end=' ')
print(f'O número {num} foi dividido {total} vezes!')
if total == 2:
    print(f'O número {num} é primo!')
else: 
    print(f'O número {num} não é primo!')

