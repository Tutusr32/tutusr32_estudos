#faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
#A) Quantas pessoas foram cadastradas
#B) Uma listagem com as pessoas mais pesadas
#C) Uma listagem com as pessoas mais leves

lista_1 = []
lista_2 = []
total = 0
peso_maior = peso_menor = 0
while True:
    lista_1.append(str(input('Digite o nome: ')))
    lista_1.append(float(input('Digite o peso: ')))
    
    if len(lista_2) == 0:
        peso_maior = peso_menor = lista_1[1]
    else:
        if peso_maior < lista_1[1]:
            peso_maior = lista_1[1]

        elif peso_menor > lista_1[1]:
            peso_menor = lista_1[1]

    lista_2.append(lista_1[:])
    lista_1.clear()
    total += 1


    continuar = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if continuar in 'n':
        break
    else:
        if continuar in 's':
            continue
        else:
            print('Escolha entre S/N !!')


print(f'Foram cadastradas {total} pessoas!')

print(f'O maior peso foi de {peso_maior}kg de:', end= ' ')
for pessoa in lista_2:
    if pessoa[1] == peso_maior:
        print(f'[{pessoa[0]}]', end= ' ')

print(f'\nO menor peso foi de {peso_menor}kg de:', end=' ')
for pessoa in lista_2:
    if pessoa[1] == peso_menor:
        print(f'[{pessoa[0]}]', end= ' ')
