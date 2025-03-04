#faça um programa de progressão aritimética v.2 usando While

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
contador = 1
termo = primeiro

while contador <= 10:
    print(f'{termo} →', end=' ')
    contador += 1
    termo += razão
print('FIM')
