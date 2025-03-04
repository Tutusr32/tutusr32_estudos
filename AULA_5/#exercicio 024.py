#faça um programa que leia o nome de uma cidade e fale se tem "Santo" no nome ou não

cidade = str(input('Qual cidade você nasceu?:')).strip()

print(cidade[0:5].lower() == 'santo')


 