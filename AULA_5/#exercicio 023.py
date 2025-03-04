#faça um programa que separe os digitos de um número entre unidade, dezena, centena e milhar

n1 = int(input('Digite um número:'))
num = str(n1)


uni = n1 // 1 % 10
dez = n1 // 10 % 10
cen = n1 // 100 % 10
mil = n1 // 1000 % 10


print(f'Analisando o número {n1}..')

print(f'Milhar: {mil}')
print(f'Centena: {cen}')
print(f'Dezena: {dez}')
print(f'Unidade: {uni}')

#também pode ser usado num = str(n1), que transforma n1 em string, podendo acompanhar {num[0]} e etc