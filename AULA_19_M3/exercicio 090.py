#faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input('Digite a média do aluno: '))

print('-=' * 30)

if aluno['Média'] < 5:
    print(f'A média é {aluno["Média"]}.')
    aluno['Situação'] = 'Reprovado'

elif aluno['Média'] >= 5 and aluno['Média'] < 7:
    print(f'A média é {aluno["Média"]}.')
    aluno['Situação'] = 'Recuperação'

elif aluno['Média'] >= 7 and aluno['Média'] <= 10:
    print(f'A média é {aluno["Média"]}.')
    aluno['Situação'] = 'Aprovado'

else:
    print('As médias devem ser entre 0 a 10!!')

print(f'Nome do Aluno: {aluno["Nome"]}.')
print(f'A média do aluno {aluno["Nome"]} é de {aluno["Média"]}.')
print(f'A situação do aluno é de {aluno['Situação']}')

