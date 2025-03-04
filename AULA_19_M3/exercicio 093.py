#crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler nome do jogador e quantas partidas ele jogou. Depois ele vai ler a quantidade de gols feito em cada partida. No final de tudo, isso será guardado em um dicionário, incluíndo o total de gols feitos durante o campeonato.

dados = {}
gols = []


dados['jogador'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas o jogador {dados["jogador"]} jogou?: '))

for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols foram feitas na {p + 1}o. partida?: ')))

dados['gols'] = gols[:]
dados['total'] = sum(gols)

print()
print(f'O nome do jogador é {dados["jogador"]}.')
print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for par, g in enumerate(gols):
    print(f'Fez {g} gols na partida {par + 1}.')
print(f'O total de gols foi: {dados["total"]}')
