#faça um programa que faça a soma de todos os números ímpares que são múltiplos de 3 de 1 até 500

soma = 0
cont = 0

for num in range(1, 501, 2):
    if num % 3 == 0:
        soma = soma + num
        cont = cont + 1
print(f'A soma de todos os {cont} números é de {soma}')
