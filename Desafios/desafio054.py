# Programa lê o ano de nascimento de 7 pessoas e diz quantas são maiores de idade e quantas menores.

from datetime import date

anoatual = date.today().year
maior = 0
menor = 0

for i in range(1, 8, 1):
    nascimento = int(input('Digite o ano de nascimento da pessoa {}: '.format(i)))
    if anoatual - nascimento < 18:
        menor = menor + 1
    else:
        maior = maior + 1
    # end-if-else
# end-for
print('Menores de idade: {}.'.format(menor))
print('Maiores de idade: {}.'.format(maior))
