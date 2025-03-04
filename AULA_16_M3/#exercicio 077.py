#crie um programa que tenha uma tupla com várias palavras (não use acentos). Depois disso, você deve mostrar pra cada palavra, suas respectivas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for vogal in palavras:
    print(f'\nNa palavra {vogal.upper()} temos as seguintes vogais:', end=' ')
    for c in vogal:
        if c in 'aeiou':
            print(c, end=' ')

