def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(f'{txt}'.center(42))
    print(linha())

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('Digite um número inteiro válido.')
            continue

        else:
            return n

def menu(lista):
    cabeçalho('Menu Principal')
    
    for i, item in enumerate(lista):
        print(f'{i+1} - {item}')

    print(linha())

    opc = leiaInt('Sua opção: ')
    return opc
