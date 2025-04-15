#Crie um código em Python que teste se o site pudim.com.br está acessível pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('O site Pudim está acessível.')

