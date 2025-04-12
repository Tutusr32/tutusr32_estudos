def leiaDinheiro(msg):
    válido = False
    while not válido:
        valor = str(input(msg)).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print(f'"{valor}" é um preço inválido!')
        else:
            válido = True
            return float(valor)
