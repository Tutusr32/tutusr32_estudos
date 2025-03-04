#aprimore o desafio #93 para que ele funcione com vários jogadores, incluíndo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
jogador = {}
partida = []


while True:
    partida.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input('Quantas partidas esse jogador fez: '))

    for c in range(0, total):
        partida.append(int(input(f'Quantos gols fez na partida {c + 1}: ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    jogadores.append(jogador.copy())

    while True:
        continuar = str(input('Deseja continuar?[S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('escolha entre S ou N.')

    if continuar in 'N':
        break

print('-=' * 30)
print('Nome',       'Gols',         'Total')


for k, v in enumerate(jogadores):
    print(f'{k:<}', end= ' ')
    for dds in v.values():
        print(f'{str(dds):<15}', end=' ')
    print()

while True:
    levantamento = int(input('Qual jogador deseja fazer o levantamento (999 para): '))
    if levantamento == 999:
        break
    if levantamento >= len(jogadores):
        print(f'Não existe jogador com o código: {levantamento}')
    else:    
        print(f'Fazendo levantamento do jogador: {jogadores[levantamento]["nome"]}')
        print(f'O Jogador se chama: {jogadores[levantamento]['nome']}: ')

        for i, g in enumerate(jogadores[levantamento]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
print('-=' * 35)

print('<<Volte sempre>>')
    
