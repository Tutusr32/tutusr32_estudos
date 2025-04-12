#Adicione ao módulo moeda.py uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from utilidadesCeV import moeda

num = float(input('Digite um número: '))

print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando em 10% é {moeda.aumento(num, 10, True)}')
print(f'Diminuindo em 10% é {moeda.diminui(num, 10, True)}')

print()
moeda.resumo(num, 10, 10)
