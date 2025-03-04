#crie um programa que leia a largura e a altura de uma parede e defina a
#quantidade de tinta que será usada (1L para 2m²)

largura = float(input('Qual é a largura da sua parede?:'))
altura = float(input('E a altura?:'))

print(f'Sua parede mede {largura*altura}m², você precisará de {(largura*altura) / 2}L de tinta para pintar a sua parede.')