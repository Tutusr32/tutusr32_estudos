#Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário informado.

from utilidadesCeV import moeda

num = float(input('Digite um número: '))

print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando em 10% é {moeda.moeda(moeda.aumento(num, 10))}')
print(f'Diminuindo em 10% é {moeda.moeda(moeda.diminui(num, 10))}')
