#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade para números reais.

def leiaint():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            return n 
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar.')


def leiafloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
            return n
        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido.')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar.')

inteiro = leiaint()
real = leiafloat()
print(f'O número inteiro digitado foi {inteiro} e o real foi {real}.')
