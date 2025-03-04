#crie um programa que leia vários valores e os coloque em uma lista. Depois disso, crie duas listas que vão conter apenas os valores pares e ímpares digitados, respectivamente. Ao final mostre a lista completa, a lista de números pares e a lista de números ímpares.

lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    if num % 2 == 0:
        lista_par.append(num)
    else:
        if num % 2 != 0:
            lista_impar.append(num)
    
    continuar = str(input('Deseja continuar?[N/S]: ')).strip().lower()[0]

    if continuar in 'n':
        break
    else:
        if continuar in 's':
            continue
        else:
            print('Escolha entre S ou N!')


lista_impar.sort()
lista_par.sort()
lista.sort()

print(f'Lista completa: {lista}')
print(f'Lista de números pares: {lista_par}')
print(f'Lista de números ímpares: {lista_impar}')

