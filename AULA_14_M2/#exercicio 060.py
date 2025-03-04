#faça um programa que leia e faça o fatorial de um número

numero = int(input('Digite um valor: '))
count = numero
fatorial = 1

print(f'Calculando fatorial de {numero}!')

while count > 0:
    print(f'{count}', end=' ')
    print('x ' if count > 1 else '= ', end='')
    fatorial *= count
    count -= 1
print(f'{fatorial}')


