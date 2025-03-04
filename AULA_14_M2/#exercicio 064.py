#faça um programa de soma de algoritimos e desconsidere o ultimo número (999)
num = contador = soma = 0

num = int(input('Digite o valor [ 999 para parar]: '))



while num != 999:
    contador += 1
    soma += num
    num = int(input('Digite o valor [ 999 para parar]: '))
print(f'Você digitou {contador} números, a soma entre eles é de {soma}!!')



