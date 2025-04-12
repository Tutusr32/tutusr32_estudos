#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from utilidadesCeV import moeda

num = float(input('Digite um número: '))

print(f'A metade de {num} é {moeda.metade(num, True)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Aumentando em 10% é {moeda.aumento(num, 10, True)}')
print(f'Diminuindo em 10% é {moeda.diminui(num, 10)}')
