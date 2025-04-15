from interface import cabeçalho

def arquivoExiste(nome):
    try:
        with open(nome, 'rt'):
            return True

    except FileNotFoundError:
        return False

def criarArquivo(nome):
    try:
        with open(nome, 'wt+') as arq:
            pass

    except:
        print('Houve um erro na criação do arquivo!')

    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        with open(nome, 'rt') as arq:
            cabeçalho('Pessoas Cadastradas.')

            for linha in arq:

                dado = linha.strip().split()
                nome = ' '.join(dado[:-2])
                idade = dado[-2]
                print(f'{nome:<30}{idade} anos')

    except:
        print('Erro ao ler o arquivo.')

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at') as a:
            a.write(f'{nome:<30}{idade} anos\n')

    except:
        print('Houve um erro na hora de escrever os dados.')
        
    else:
        print(f'Novo registro de {nome} adicionado.')
