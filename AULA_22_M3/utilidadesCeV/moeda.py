# Conjunto de bibliotecas do exercício 107, 108 e 109

def dobro(n, formato=False):
    resultado = n * 2
    if formato:
        return moeda(resultado)
    else:
        return resultado

def metade(n, formato=False):
    resultado = n / 2
    if formato:
        return moeda(resultado)
    else:
        return resultado

def aumento(n, desc, formato=False):
    resultado = n + (n * desc / 100)
    if formato:
        return moeda(resultado)
    else:
        return resultado

def diminui(n, desc, formato=False):
    resultado = n - (n * desc / 100)
    if formato:
        return moeda(resultado)
    else:
        return resultado

def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(n, desc1, desc2):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do Preço: \t{dobro(n, True)}')
    print(f'Metade do Preço: \t{metade(n, True)}')
    print(f'{desc1}% de aumento: \t{aumento(n, desc1, True)}')
    print(f'{desc2}% de redução: \t{diminui(n, desc2, True)}')
    print('-' * 30)
