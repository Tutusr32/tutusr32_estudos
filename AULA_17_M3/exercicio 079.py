#crie um programa onde o usuário possa adicionar valores numéricos e adiciona-los em uma lista. Caso o número for repetido, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor repetido, não cadastrado!')

    continuar = str(input('Deseja continuar? [N/S]: ')).strip().lower()[0]
    if continuar in 'n':
        break
    else:
        if continuar in 's':
            continue
        else:
            print('Escolha entre [N/S]!')

lista.sort()
print(f'Você digitou os seguintes valores: {lista}')

