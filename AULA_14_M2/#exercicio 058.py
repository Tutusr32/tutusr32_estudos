#faça um jogo da adivinhação usando while
from random import randint

computador = randint(0,10)

print('O computador acabou de pensar em um número de 0 a 10, tente adivinha-lo!!')

tentativas = 0

acertou = False

while not acertou:
    numero = int(input('Digite o número do seu palpite: '))
    tentativas += 1
    if numero == computador:
        acertou = True
        print(f'Parabéns, você acertou com {tentativas} tentativas!')
    else:
        if numero > computador:
            print('Menos, tente mais um palpite!')
        elif numero < computador:
            print('Mais, tente mais um palpite!')


