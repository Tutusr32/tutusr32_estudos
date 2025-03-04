#faça um programa que gerencie os pagamentos de uma loja

preço = float(input('Qual o preço das compras (R$)?:'))

forma = int(input('''
[ 1 ] À vista no dinheiro/cheque
[ 2 ] No cartão à vista
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
'''))

parcela = preço / 2

if forma == 1:
    print(f'Sua compra de R${preço}, ficou um total de R${preço - (preço*10) / 100} com 10% de desconto!')
elif forma == 2:
    print(f'Sua compra de R${preço}, ficou um total de R${preço - (preço*5) / 100} com 5% de desconto!')
elif forma == 3:
    print(f'Sua compra ficou parcelada em 2x P{parcela}!')
    print(f'Sua compra ficou um total de R${preço}!')
elif forma == 4:
    print(f'Sua compra de {preço}, ficou um total de R${preço + (preço*20) / 100} com 20% de juros!')
else:
    print('Você deve informar entre um número de 1 até 4 para selecioar a forma de pagamento!!')
