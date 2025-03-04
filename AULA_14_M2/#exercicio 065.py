#faça um programa que leia números e dê opção de continuidade, ao fim do programa entregue a média e o menor e maior número que foi lido

contador = num = média = soma = maior = menor = 0
resp = 'S'

while resp in 'Ss':
    num = int(input('Digite um valor: '))
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    resp = str(input('Você quer continuar: [S/N]: ')).strip()

media = soma / contador
print(f'Você digitou {contador} números, a média entre eles é de {media}.')
print(f'O maior número foi de {maior} e o menor foi de {menor}.')

