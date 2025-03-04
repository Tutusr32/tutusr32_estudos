#faça um programa que leia 6 números e faça soma dos números pares e desconsidere os ímpares

soma = 0

for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:    
        soma = soma + num
print(f'A soma de somente os números pares é de {soma}')
