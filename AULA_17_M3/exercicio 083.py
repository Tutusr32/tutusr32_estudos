#crie um programa que o usuário digite um expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressão = str(input('Digite a sua expressão: '))
lista = []

for simbolo in expressão:
    if simbolo == '(':
        lista.append('(')

    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')

