#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:   Quantidade de notas, A maior nota, A menor nota, A média, A situação(opcional) e as docstrings.

def notas(*num, sit=False):
    """
    Função para analisar notas de alunos e retornar um dicionário com informações sobre as notas e a situação.

    Parâmetros:
    - *num: Notas dos alunos (valores numéricos), podendo ser um número variável de notas.
    - sit (opcional): Se True, inclui a situação do aluno com base na média das notas. Caso contrário, não inclui a situação.
    
    Retorna:
    - Dicionário contendo:
        - 'total': Quantidade de notas informadas.
        - 'maior': A maior nota fornecida.
        - 'menor': A menor nota fornecida.
        - 'media': A média das notas.
        - 'situação' (se sit=True): A situação do aluno, que pode ser 'RUIM', 'RAZOÁVEL' ou 'BOA', baseada na média.
    
    Exemplo de uso:
    >>> notas(5.5, 7.0, 8.0, 6.5, sit=True)
    {'total': 4, 'maior': 8.0, 'menor': 5.5, 'media': 6.75, 'situação': 'RAZOÁVEL'}
    
    Se nenhuma nota for informada:
    >>> notas()
    'Nenhum valor foi informado.'
    """
    
    if len(num) == 0:
        return 'Nenhum valor foi informado.'

    total_notas = len(num)
    maior_nota = max(num)
    menor_nota = min(num)
    media = sum(num) / total_notas
    
    resp = {
        'total': total_notas,
        'maior': maior_nota,
        'menor': menor_nota,
        'media': media
    }

    if sit:
        if media < 6:
            resp['situação'] = 'RUIM.'

        elif media >= 6 and media < 7:
            resp['situação'] = 'RAZOÁVEL.'

        elif media > 7 and media <= 10:
            resp['situação'] = 'BOA.'
        else:
            print('A média máxima é 10.')

    return resp


#help(notas)

resp = notas(10, 8, 8, 10, sit=True)
print(resp)
