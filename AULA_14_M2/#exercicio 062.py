#faça uma super progressão aritimética usando While, adicione a opção de mostrar mais termos ao programa 

from time import sleep

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
contador = 1
termo = primeiro
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} →', end=' ')
        contador += 1
        termo += razão
    print('PAUSA')
    mais = int(input('Quantos termos adicionais deseja adicioar: '))
print(f'Progressão finalizada com {total} termos mostrados ao todo!!')


