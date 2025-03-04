#   faça um programa que conte e some vários valores recebidos. (use Break!!)
#   use (999) para parar o programa, desconsidere ele na soma e no contador.

soma = contador = n = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    contador += 1
    if n == 999:
        break
    soma += n
print(f'Você digitou {contador - 1} números, a soma entre eles é de {soma}.')
