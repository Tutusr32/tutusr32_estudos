#exercicio 004
#faça um programa que revele todos as informações de um valor e seu tipo:

n1 = input('Digite algo:')

print('tipo primitivo desse valor:', type(n1))
print('ele é alfanúmerico?:', n1.isalnum())
print('ele é uma letra, palavra e etc?:', n1.isalpha())
print('ele é um número?:', n1.isnumeric())
print('ele está todo no diminutivo?:', n1.islower())
print('ele está todo no aumentativo?:', n1.isupper())
print('ele é printavél?:', n1.isprintable())

#assim, ele irá printar todas as informações no terminal.

