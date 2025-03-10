#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome=False, gols=0):

    if gols in '':
        gols = '0'
    if not gols.isnumeric():
        gols = '0'


    if nome in '':
        print(f'O jogador <Desconhecido> marcou {gols} gols na temporada.')
    else:
        print(f'O jogador {nome} marcou {gols} gols na temporada.')


nome = str(input('Nome do jogador: '))
gols = str(input('Gols: '))
ficha(nome, gols)
