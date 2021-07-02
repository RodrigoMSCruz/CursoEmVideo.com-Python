# Módulo chamado moeda.py que tem as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Também há um programa que importa esse módulo e use algumas dessas funções.

import moeda
#from desafio107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}.')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}.')
print(f'Aumentando em 10%, temos R$ {moeda.aumentar(p, 10)}')
