#crie um programa que leia vários valores e os coloque em uma lista. Depois disso mostre:
#A) Quantos números foram digitados:
#B) A lista de valores ordenada de forma decrescente
#C) Se o valor 5 está ou não na lista

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar?[N/S]: ')).strip().lower()[0]


    if continuar in 'n':
        break
    else:
        if continuar in 's':
            continue
        else:
            print('Escolha entre N ou S!!!')

print(f'Foram digitados {len(lista)} elementos.')

lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente: {lista}')

if 5 not in lista:
    print('O número 5 não foi encontrado!')
else:
    if 5 in lista:
        print('O número 5 faz parte da lista!')
