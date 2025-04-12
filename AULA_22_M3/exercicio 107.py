#Crie um módulo chamado moeda.py que tenha as funções incorporadas: dobro(), metade(), aumento() e diminui(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from utilidadesCeV import moeda

num = float(input('Digite um número: '))

print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Aumentando em 10% é {moeda.aumento(num, 10)}')
print(f'Diminuindo em 10% é {moeda.diminui(num, 10)}')
