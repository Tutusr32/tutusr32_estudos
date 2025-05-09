#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. 
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessaos cadastradas

from interface import *
from arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        lerArquivo(arq)

    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
        
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)


