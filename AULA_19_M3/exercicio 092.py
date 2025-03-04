#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
ano = datetime.now().year

dados = {}

dados['nome'] = str(input('NOME: ')).capitalize()
dados['nascimento'] = int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['carteira'] != 0:
    dados['contrat'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contrat'] - dados['nascimento']) + 35
else:
    print()
idade = ano - dados['nascimento'] 
print('-=' * 35)

for k, v in dados.items():
    print(f' -{k} tem valor: {v}')
