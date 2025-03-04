#faça um programa que peça um número, e dê opções para converter a base, sendo binario, octal e hexadecimal

num = int(input('Digite um número:'))
print('''
Escolha uma base para conversão:
1 - Binaria.
2 - Octal.
3 - Hexadecimal.
''')
opçao = int(input('Sua opção:'))

if opçao == 1:
    print(f'{num} convertido para Binário é {bin(num)[2:]}!')
elif opçao == 2:
    print(f'{num} convertido para Octal é {oct(num)[2:]}!')
elif opçao == 3:
    print(f'{num} convertido para Hexadecimal é {hex(num)[2:]}!')

else:
    print('Selecione uma opção de 1 até 3!!')
