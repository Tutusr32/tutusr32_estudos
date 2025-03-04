#faça um programa que calcule uma média de 2 notas e diga se foi aprovado, está de recuperação ou reprovado

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média é de {media}. Reprovado!')
elif media >= 5 and media <= 6.9:
#também pode ser usado elif 7 > media >= 5: para este elif de recuperação.
    print(f'Sua média é de {media}. Recuperação!')
else: 
    print(f'Sua média é de {media}. Aprovado!')
    