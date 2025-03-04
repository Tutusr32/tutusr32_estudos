#faça um programa que indentifique se tem 'Silva' no nome de uma pessoa ou não

nome = str(input('Qual é o seu nome?:')).strip()

if 'silva' in nome.lower().split():
    print('Tem Silva no nome!')
else:
    print('Não tem silva no nome!!')

#também pode ser usado: print(f'Tem silva no nome? {'Silva in nome.lower().split()'}')
    
