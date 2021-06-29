# Código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request
from time import sleep


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLErrot:
    print('Erro! Site Pudim não está acessível.')
else:
    print('O site Pudim acessível.')
    sleep(2)
    print(site.read())