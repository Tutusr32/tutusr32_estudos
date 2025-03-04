#desenvolva um programa que leia 4 valores e os armazene em uma tupla, no final mostre:
#A) Quantas vezes aparece o número 9
#B) Em qual posição aparece o número 3
#C) Quais foram os números pares

num = (
int(input('Digite um valor: ')), 
int(input('Digite mais um valor: ')), 
int(input('Digite mais um valor: ')), 
int(input('Digite o último valor: ')), 
)


print(f'Você digitou os valores: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece na posição {num.index(3) +1}')
else:
    print('O número 3 não foi digitado.')
print(f'Os valores pares foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
