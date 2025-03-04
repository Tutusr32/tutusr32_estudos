#faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    print('-' * (len(txt) + 4))
    print(f'  {txt}')
    print('-' * (len(txt) + 4))

escreva('Arthur')
escreva('Gustavo Guanabara')
escreva('Python é muito interessante')

