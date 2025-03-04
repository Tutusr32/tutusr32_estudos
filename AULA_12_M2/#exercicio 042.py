#faça um programa que classifique um triangulo


r1 = float(input('Primeira reta:'))
r2 = float(input('Segunda reta:'))
r3 = float(input('Terceira reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os seguimentos {r1}, {r2} e {r3}, podem formar um triangulo')


    if r1 == r2 and r2 == r3:
        print('Os seguimentos formam um triangulo Equilátero')
    elif r1 != r2 and r2 != r3:
        print('Os seguimentos formam um triangulo Escaleno')
    else:
        print('Os segmentos formam um triangulo Isósceles')
    

else:
    print('Não podem formar um triangulo')
    


