#faça um programa que conte as letras A em uma frase, fale sua primeira aparição e última

frase = str(input('Digite uma frase:')).upper().strip()

print(f'A letra A aparece {frase.count('A')} vezes na frase!')

print(f'A primeira letra A aparece na posição {frase.find('A')+1}!')

print(f'O ultimo A aparece na posição {frase.rfind('A')+1}!')


