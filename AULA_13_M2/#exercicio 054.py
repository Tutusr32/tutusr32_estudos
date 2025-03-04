#faça um programa que detecte os menore e os maiores de idade em um grupo de 7 pessoas
from datetime import date

ano = date.today().year
demaior = 0
demenor = 0

for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nasc da {c}º pessoa: '))
    idade = ano - nasc
    if idade >= 18:
        demaior = demaior + 1
    else:
        demenor = demenor + 1
        
print(f'Temos {demaior} pessoas maiores de idade')
print(f'Temos {demenor} pessoas menor de idade')
