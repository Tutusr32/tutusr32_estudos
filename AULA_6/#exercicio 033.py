#faça um programa que diga o menor e o maior número


n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
n3 = int(input('Terceiro valor:'))

#ifs para o menor
if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')

elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor número é {n3}')

#ifs para o maior
if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
elif n3 > n1 and n3 > n2 :
    print(f'O maior número é {n3}')    
