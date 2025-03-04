#Crie um programa que leia nome, idade e sexo de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com mulheres
#D) Uma lista com idade acima da média

pessoa = {}
dados = []
contador = 0
idade = []


while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['idade'] = int(input('Idade: '))

    while True:
        pessoa['sexo'] = str(input('Digite [F/M]: ')).upper()[0]

        if pessoa['sexo'] in 'MF':
            break
        print(f'ERRO! Selecione entre F ou M.')

    dados.append(pessoa.copy())
    idade.append(pessoa['idade'])
    contador += 1

    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if continuar in 'N':
        break

média = sum(idade) / contador


print(f'Foram cadastradas {contador} pessoas.')
print(f'A média da idade entre elas é de {média:.2f} anos.')
print(f'As mulheres da lista, são: ', end= ' ')

for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()    

print(f'As pessoas com idades acima da média, são: ', end= ' ')
for i in dados:
    if i['idade'] > média:
        print(f'{i['nome']}', end= ' ')

        