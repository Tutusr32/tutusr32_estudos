#faça um programa que faça os termos da sequência de Fibonacci usando While

num = int(input('Quantos termos você quer mostrar?: '))
a = 0
b = 1
c = 0
contador = 0

while contador < num:
    print(f'{c}', end=' → ')
    a = b
    b = c
    c = a + b
    contador += 1
print('FIM')
