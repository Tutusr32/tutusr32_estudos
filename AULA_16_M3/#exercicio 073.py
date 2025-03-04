#crie uma tupla preenchida com os 20 times do brasileirão em ordem de colocação e depois mostre:
#A) Os 5 primeiros colocados
#B) Os 4 ultimos colocados
#C) Os times em ordem alfabética
#D) Posição do São Paulo FC

times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Bahia', 'São Paulo', 'Cruzeiro', 'Atlético-MG', 'Atlhetico-PR', 'Vasco da Gama', 'Juventude', 'Bragantino', 'Internacional', 'Criciúma', 'Grêmio', 'EC Vitória', 'Corinthians', 'Fluminense', 'Cuiabá', 'Atlético-GO')

print('-=-' * 40)
print(f'Lista de times do Brasileirão: {times}')
print('-=-' * 40)
print(f'Lista dos 5 primeiros colocados: {times[0:5]}')
print('-=-' * 40)
print(f'Lista dos 4 últimos colocados: {times[-4:]}')
print('-=-' * 40)
print(f'Lista dos times em ordem alfabética: {sorted(times)}')
print('-=-' * 40)
print(f'O São Paulo está na posição {times.index('São Paulo')+ 1}')
print('-=-' * 40)
      