#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesCeV import moeda, dado

num = dado.leiaDinheiro('Digite o preço: ')
moeda.resumo(num, 13, 26)
