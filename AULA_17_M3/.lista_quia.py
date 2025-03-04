#listas

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

membros_slipknot = ['Sid Wilson', 'Joey Jordison', 'Paul Gray', 'Chris Fehn', 'James Root', 'Craig Jones', 'Shawn Crahan', 'Mick Thomson', 'Corey Taylor']

valores = [8, 2, 5, 4, 9, 3, 0]

lanche_2 = []

#comandos:

#adicionar:

lanche.append('Cookie')  #adiciona itens no final de uma lista, 'Cookie' entrou no final da lista, atrás de pudim

lanche.insert(0, 'Cachorro-Quente')   #adiciona um item na lista em qualquer posição, nesse caso 'Cachorro-Quente' entra na posição 0

#deletar:

del membros_slipknot[1]   #deleta um elemento da lista, nesse caso, 'Joey Jordison' foi deletado

membros_slipknot.pop(1)       #também deleta elementos de uma lista, nesse caso, 'Paul Gray' foi deletado, pois 'Joey Jordison' ja tinha sido deletado, então 'Paul Gray' ficou na posição 1 na lista

lanche.pop()        #remove o último item da lista, 'Cookie'

lanche.remove('Pudim')      #remove um item da lista pelo nome.

#organização:

valores = list(range(4, 11))        #cria uma lista de números do 4 ao 10 de forma crescente

valores.sort()                 #cria uma lista de números organizada '[8, 2, 5, 4, 9, 3, 0]' vira [0, 2, 3, 4, 5, 8, 9]

valores.sort(reverse=True)     #cria uma lista de números organizada de forma reversa '[8, 2, 5, 4, 9, 3, 0]' vira [9, 8, 5, 4, 3, 2, 0]


len(valores)        #conta o número de valores em uma lista,   len(valores) = 7

valores.index(8) + 1      #mostra a posição de um elemento da lista, nesse caso, mostra a posição do número 8

lanche_2.append(lanche[:])      #cria uma cópia de uma lista

print(lanche)
print('-' * 45)
print(membros_slipknot)
print('-' * 45)
print(valores)
print('-' * 45)
print(lanche_2)