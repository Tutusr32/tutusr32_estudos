#faça um programa IMC de uma pessoa

Altura = float(input('Qual é a sua altura?:'))
Peso = float(input('qual é o seu peso?:'))

imc = Peso / Altura**2

if imc < 18.5:
     print('abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
      print('Peso normal')
elif imc >= 25 and imc <= 29.9:
      print('Sobrepeso')
elif imc >= 30 and imc <= 34.9:
      print('Obesidade Grau 1')
elif imc >= 35 and imc <= 39.9:
       print('Obesidade grau 2')
else:
        print('Obesidade grau 3')

print(f'Seu IMC é de {imc}!')