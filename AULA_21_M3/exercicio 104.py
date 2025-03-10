#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor númerico. Ex: n = leiaint('Digite um n'). (sem usar tratamento de exceções.)

def leiaint(msg):
    vál = False
    valor = 0
    while True:
        n = str(input(msg))

        if n.isnumeric():
            valor = int(n)
            vál = True
        else:
            print('ERRO! Digite um valor válido.')
        
        if vál:
            break

    return valor

n = leiaint('Digite um número: ')
print(f'O número digitado foi {n}.')
