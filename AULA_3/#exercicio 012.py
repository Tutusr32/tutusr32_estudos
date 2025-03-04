#crie um programa que peça o valor do produto e quanto sairá com um X de desconto

produto = input('Qual é o seu produto?:')
preço = float(input('Qual é o preço dele?: R$'))
desconto = float(input('Quanto ele tem de desconto?'))

print(f'Seu produto {produto} custa {preço}!')
print(f'Com desconto de {desconto}%, ele ficará R${preço - (preço*desconto) / 100}!!')

