#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
#o programa deverá ler um número entre 0 a 20 e escreve-lo por extenso.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente: ')
print(f'você digitou o número {extenso[num]}!')
