#faça um programa que fale o primeiro e o ultimo nome de uma pessoa

nom = str(input('Qual é o seu nome?:')).strip()

nome = nom.split()

print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)- 1]}')


