#crie um programa onde o usuário digite 5 valores numéricos e os cadastre em uma lista. já na posição correta de inserção (sem usar o sort.()). No final, mostre a lista ordenada na tela.

lista = []
menor = maior = 0

for valores in range(0, 5):
    num = int(input('Digite um valor: '))
    if valores == 0:
        lista.append(num)
        print('Número sendo adicionado ao final da lista..')

    elif num > lista[-1]:
        lista.append(num)
        print('Número sendo adicionado ao final da lista..')
    else:
        posição = 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição, num)
                break
            posição += 1
        print(f'Número sendo adicionado na posição: {posição}')

print(f'Os valores digitados foram: {lista}')

